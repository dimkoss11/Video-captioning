import os

from nn.utils.extract_clips import extract_clips
from nn.utils.save_captions import save_captions
from nn.utils.delete_files import delete_files

from nn.utils.add_audio_to_video import add_audio_to_video
from nn.utils.unite_audio import unite_audio
from nn.utils.translate_and_voice_final import translate_and_voice

from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks


def main(root_path, videos_path):

    model_id = 'damo/multi-modal_hitea_video-captioning_base_en'
    pipeline_caption = pipeline(Tasks.video_captioning, model=model_id, device='cuda')
    all_result_lists = extract_clips(root_path, 50)

    for path, folders, files in os.walk(os.path.join(root_path, videos_path)):
        for scene in files:
            video, clip = os.path.normpath(path).split('\\')[-2:]
            scene_path = os.path.join(path, scene)
            
            start = all_result_lists[video + '.mp4'][clip + '.mp4'][scene]['start']
            end = all_result_lists[video + '.mp4'][clip + '.mp4'][scene]['end']
            min_length = int((end - start) * 1.3)
            
            pipeline_caption.model.model.beam_generator.min_length = min_length
            pipeline_caption.model.model.beam_generator.beam_size = 20
            output = pipeline_caption(scene_path)
            all_result_lists[video + '.mp4'][clip + '.mp4'][scene].update(output)

    save_captions(root_path, all_result_lists)
    translate_and_voice(root_path, all_result_lists)
    unite_audio(root_path, all_result_lists)
    add_audio_to_video(root_path)
    

if __name__ == '__main__':
    root_path = 'inference_videos'
    videos_path = 'clips'
    main(root_path, videos_path)
    delete_files(root_path)
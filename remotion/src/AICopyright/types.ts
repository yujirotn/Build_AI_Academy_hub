export interface SubtitleSegment {
  text: string;
  startMs: number;
  endMs: number;
}

export interface SlideData {
  id: number;
  image: string;
  audio: string;
  subtitles: SubtitleSegment[];
  durationSec: number;
  durationFrames: number;
  startFrame: number;
  gapAfterFrames: number;
}

export interface SubtitleStyle {
  fontFamily: string;
  fontSize: number;
  fontWeight: string;
  color: string;
  backgroundColor: string;
  padding: number;
  borderRadius: number;
  position: string;
  marginBottom: number;
  maxWidth: number;
}

export interface ImageStyle {
  fit: string;
  backgroundColor: string;
}

export interface TransitionStyle {
  type: string;
  durationFrames: number;
}

export interface AudioStyle {
  volume: number;
  fadeInFrames: number;
  fadeOutFrames: number;
}

export interface ProjectStyle {
  subtitle: SubtitleStyle;
  image: ImageStyle;
  transition: TransitionStyle;
  audio: AudioStyle;
}

export interface ProjectMeta {
  title: string;
  description: string;
  fps: number;
  width: number;
  height: number;
  totalFrames: number;
  totalDurationSec: number;
  assetsPath: string;
  audioPath: string;
}

export interface ProjectData {
  meta: ProjectMeta;
  style: ProjectStyle;
  slides: SlideData[];
}

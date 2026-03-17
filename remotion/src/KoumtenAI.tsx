import React from "react";
import { AbsoluteFill, Sequence } from "remotion";
import { z } from "zod";
import { Slide } from "./AICopyright/Slide";
import { ProjectData } from "./AICopyright/types";
import projectData from "../public/工務店のAI社内推進の仕方/工務店のAI社内推進の仕方_project.json";

const AUDIO_DELAY_FRAMES = 30; // 音声開始まで1秒の遅延

export const koumtenAISchema = z.object({});

export const KoumtenAI: React.FC<z.infer<typeof koumtenAISchema>> = () => {
  const data = projectData as ProjectData;

  return (
    <AbsoluteFill style={{ backgroundColor: data.style.image.backgroundColor }}>
      {data.slides.map((slide, index) => (
        <Sequence
          key={slide.id}
          from={slide.startFrame}
          durationInFrames={slide.durationFrames + slide.gapAfterFrames + AUDIO_DELAY_FRAMES}
        >
          <Slide
            slide={slide}
            style={data.style}
            assetsPath={data.meta.assetsPath}
            audioPath={data.meta.audioPath}
          />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};

export { projectData as koumtenProjectData };

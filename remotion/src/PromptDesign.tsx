import React from "react";
import { AbsoluteFill, Sequence } from "remotion";
import { z } from "zod";
import { Slide } from "./AICopyright/Slide";
import { ProjectData } from "./AICopyright/types";
import projectData from "../public/AIを上手に扱うポイント_プロンプト設計/AIを上手に扱うポイント_プロンプト設計_project.json";

const AUDIO_DELAY_FRAMES = 30; // 音声開始まで1秒の遅延

export const promptDesignSchema = z.object({});

export const PromptDesign: React.FC<z.infer<typeof promptDesignSchema>> = () => {
  const data = projectData as ProjectData;

  return (
    <AbsoluteFill style={{ backgroundColor: data.style.image.backgroundColor }}>
      {data.slides.map((slide) => (
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

export { projectData as promptDesignProjectData };

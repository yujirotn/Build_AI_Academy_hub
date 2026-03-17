import React from "react";
import { AbsoluteFill, Sequence } from "remotion";
import { z } from "zod";
import { Slide } from "./AICopyright/Slide";
import { ProjectData } from "./AICopyright/types";
import projectData from "../public/Geminiで営業ロープレを強化する方法/Geminiで営業ロープレを強化する方法_project.json";

const AUDIO_DELAY_FRAMES = 30; // 音声開始まで1秒の遅延

export const geminiSalesRoleplaySchema = z.object({});

export const GeminiSalesRoleplay: React.FC<z.infer<typeof geminiSalesRoleplaySchema>> = () => {
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

export { projectData as geminiProjectData };

import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import { SubtitleStyle } from "./types";

interface SubtitleProps {
  text: string;
  style: SubtitleStyle;
}

export const Subtitle: React.FC<SubtitleProps> = ({ text, style }) => {
  const frame = useCurrentFrame();

  const opacity = interpolate(frame, [0, 5], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        justifyContent: "flex-end",
        alignItems: "center",
        paddingBottom: style.marginBottom,
      }}
    >
      <div
        style={{
          fontFamily: style.fontFamily,
          fontSize: style.fontSize,
          fontWeight: style.fontWeight as "bold" | "normal",
          color: style.color,
          backgroundColor: style.backgroundColor,
          padding: style.padding,
          borderRadius: style.borderRadius,
          maxWidth: style.maxWidth,
          textAlign: "center",
          opacity,
        }}
      >
        {text}
      </div>
    </AbsoluteFill>
  );
};

import "./index.css";
import { Composition } from "remotion";
import { AICopyright, aiCopyrightSchema, projectData } from "./AICopyright";
import { GeminiSalesRoleplay, geminiSalesRoleplaySchema, geminiProjectData } from "./GeminiSalesRoleplay";
import { KoumtenAI, koumtenAISchema, koumtenProjectData } from "./KoumtenAI";
import { AIAdKeihin, aiAdKeihinSchema, aiAdKeihinProjectData } from "./AIAdKeihin";
import { SeiseiAI, seiseiAISchema, seiseiAIProjectData } from "./SeiseiAI";
import { PromptDesign, promptDesignSchema, promptDesignProjectData } from "./PromptDesign";

// Each <Composition> is an entry in the sidebar!

export const RemotionRoot: React.FC = () => {
  return (
    <>
      {/* AI活用と著作権 講座動画 */}
      <Composition
        id="AICopyright"
        component={AICopyright}
        durationInFrames={projectData.meta.totalFrames}
        fps={projectData.meta.fps}
        width={projectData.meta.width}
        height={projectData.meta.height}
        schema={aiCopyrightSchema}
        defaultProps={{}}
      />

      {/* Geminiで営業ロープレを強化する方法 */}
      <Composition
        id="GeminiSalesRoleplay"
        component={GeminiSalesRoleplay}
        durationInFrames={geminiProjectData.meta.totalFrames}
        fps={geminiProjectData.meta.fps}
        width={geminiProjectData.meta.width}
        height={geminiProjectData.meta.height}
        schema={geminiSalesRoleplaySchema}
        defaultProps={{}}
      />

      {/* 工務店のAI社内推進の仕方 */}
      <Composition
        id="KoumtenAI"
        component={KoumtenAI}
        durationInFrames={koumtenProjectData.meta.totalFrames}
        fps={koumtenProjectData.meta.fps}
        width={koumtenProjectData.meta.width}
        height={koumtenProjectData.meta.height}
        schema={koumtenAISchema}
        defaultProps={{}}
      />

      {/* AI広告と景品表示法 */}
      <Composition
        id="AIAdKeihin"
        component={AIAdKeihin}
        durationInFrames={aiAdKeihinProjectData.meta.totalFrames}
        fps={aiAdKeihinProjectData.meta.fps}
        width={aiAdKeihinProjectData.meta.width}
        height={aiAdKeihinProjectData.meta.height}
        schema={aiAdKeihinSchema}
        defaultProps={{}}
      />
      {/* 生成AIとは何か */}
      <Composition
        id="SeiseiAI"
        component={SeiseiAI}
        durationInFrames={seiseiAIProjectData.meta.totalFrames}
        fps={seiseiAIProjectData.meta.fps}
        width={seiseiAIProjectData.meta.width}
        height={seiseiAIProjectData.meta.height}
        schema={seiseiAISchema}
        defaultProps={{}}
      />
      {/* AIを上手に扱うポイント：プロンプト設計 */}
      <Composition
        id="PromptDesign"
        component={PromptDesign}
        durationInFrames={promptDesignProjectData.meta.totalFrames}
        fps={promptDesignProjectData.meta.fps}
        width={promptDesignProjectData.meta.width}
        height={promptDesignProjectData.meta.height}
        schema={promptDesignSchema}
        defaultProps={{}}
      />
    </>
  );
};

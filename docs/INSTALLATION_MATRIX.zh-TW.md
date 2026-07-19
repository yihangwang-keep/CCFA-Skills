# 安裝矩陣

依使用者可見能力安裝。通訊設計驗證閉環只保留四個執行入口：Phase A、Phase B 和兩個獨立程式碼 auditor。

| 套件 | Skills | 能力 |
| --- | --- | --- |
| 完整研究流程 | 全部 19 個 runtime skills | 從 idea 到 rebuttal，包含兩個通訊階段和治理能力。 |
| 通訊設計驗證 | `ccf-common`, `ccf-pipeline-orchestrator`, `ccf-mes-validation`, `ccf-complexity-upgrade`, `ccf-env-code-auditor`, `ccf-algorithm-code-auditor` | 完成 Phase A、Phase B、獨立稽核和修復閉環。 |
| 早期研究 | `ccf-common`, `ccf-pipeline-orchestrator`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-mes-validation`, `ccf-complexity-upgrade`, `ccf-env-code-auditor`, `ccf-algorithm-code-auditor` | idea、文獻、問題/MES/演算法驗收、複雜度升級和證據計畫。 |
| 圖表與正文 | `ccf-common`, `ccf-pipeline-orchestrator`, `ccf-visual-composer`, `ccf-paper-writer`, `ccf-integrity-auditor`, `ccf-submission-checker` | 證據計畫、真實結果圖表、正文、一致性和投稿檢查。 |

Phase A 包含初始問題文件、最小但完整的 MES/環境、初始演算法、稽核和修復。Phase B 讀取已接受的 MES、現有程式碼和結果，寫升級場景文件，直接修改並稽核現有環境，再修改和修復演算法；Phase B 不再建立 MES，也不要求先執行未修改的原演算法基線。

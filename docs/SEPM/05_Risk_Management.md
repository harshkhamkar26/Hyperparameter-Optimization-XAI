# Risk Management

| ID | Risk | Probability | Impact | Mitigation |
|---|---|---|---|---|
| R1 | Dataset is unsuitable or incomplete | Medium | High | Validate multiple candidate datasets before final selection |
| R2 | Optimization takes too long | Medium | Medium | Limit trials, use cross-validation carefully and reduce search space |
| R3 | Model overfits | Medium | High | Use validation, cross-validation and appropriate regularization |
| R4 | XAI output is misunderstood | Medium | Medium | Document interpretation and limitations clearly |
| R5 | Software/library compatibility issue | Medium | Medium | Pin/test dependencies and maintain a reproducible environment |
| R6 | Results cannot be reproduced | Low | High | Fix seeds, document configuration and record experiment settings |
| R7 | Project schedule slips | Medium | High | Use milestones and prioritize core requirements |
| R8 | Dataset licensing/privacy issue | Low | High | Verify license and avoid sensitive/private data |
| R9 | Baseline does not improve after tuning | Medium | Medium | Compare multiple reasonable search spaces and report negative findings honestly |
| R10 | Documentation becomes inconsistent with implementation | Medium | Medium | Update SEPM documents at each major milestone |

## Risk Response Strategy
Risks are monitored throughout the project. High-impact risks receive priority, and mitigation actions are reviewed at each project milestone.

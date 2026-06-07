# 00 · 项目上下文 〔本项目活记忆 · AI 维护〕

> **作用**:这是项目的"身份档案"。AI 接管项目时先读这里,了解项目目标、技术栈、目录、部署取值。
> **更新时机**:架构、技术栈、目录结构、端口、部署目录、重要约束变化时更新。

---

## 1. 项目是什么

- **项目名称**:`AICoding_bank`
- **一句话目标**:基于银行营销数据构建一个 Streamlit Web 应用,提供数据分析交互页面与在线认购预测系统。
- **使用者/受益者**:银行营销分析师(数据分析)、业务人员(快速预测客户是否会认购定期存款)。
- **核心功能**:
  - 数据分析交互页面:探索性数据分析(EDA),展示数据分布、特征相关性、可视化图表。
  - 在线预测系统:基于离线训练的模型,用户通过点选输入客户特征,实时预测是否认购。
- **输入/数据**:银行营销数据集(`data/train.csv` 22,500 行 × 20 特征,无标签;`data/test.csv` 7,500 行 × 20 特征 + `subscribe` 标签)。包含人口统计、联系方式、宏观经济指标等特征。数据不进 Git。

## 2. 技术栈

| 层 | 选型 | 理由 |
|---|---|---|
| 语言/运行时 | Python 3.11 | 数据科学与 ML 生态成熟,团队熟悉 |
| Web 框架 | Streamlit | 快速构建数据应用,原生支持多页面 |
| ML | scikit-learn | 轻量、无需 GPU,适合表格数据分类任务 |
| 数据处理 | pandas + numpy | Python 数据标准栈 |
| 可视化 | plotly / matplotlib | 交互式图表,Streamlit 原生兼容 |
| 测试 | pytest | Python 最流行测试框架 |
| 格式/静态检查 | ruff | 快速、单一工具替代 flake8+black |
| 打包/运行 | Docker | 一键部署,环境一致 |
| CI/CD | GitHub Actions (仅 CI) | 通用、可视化、适合教学与团队协作 |

## 3. 目录地图

```text
AICoding_bank/
├── standards/                 # AI 项目记忆与通用规范
├── src/
│   ├── app.py                 # Streamlit 主入口(多页面应用)
│   ├── pages/
│   │   ├── 1_数据分析.py       # 数据分析交互页面
│   │   └── 2_在线预测.py       # 在线预测系统页面
│   ├── ml/
│   │   ├── train.py           # 离线模型训练脚本
│   │   ├── preprocess.py      # 数据预处理管道
│   │   └── predict.py         # 预测接口函数
│   └── utils/
│       └── data.py            # 数据加载工具
├── tests/
│   ├── test_preprocess.py
│   ├── test_predict.py
│   └── test_data.py
├── artifacts/
│   └── model.pkl              # 训练产出的模型文件(.gitignore 排除)
├── data/                      # 原始数据集(.gitignore 排除)
│   ├── train.csv
│   └── test.csv
├── .streamlit/
│   └── config.toml            # Streamlit 配置(端口等)
├── requirements.txt           # 生产运行依赖
├── requirements-dev.txt       # CI/本地检查依赖
├── Dockerfile
├── .gitignore
├── .github/workflows/
│   └── ci.yml
├── README.md
└── standards/
    ├── PROGRESS.md
    └── ...
```

> 新增目录前先更新本节,避免项目越做越散。

## 4. 质量门槛

| 类型 | 本项目标准 |
|---|---|
| 格式检查 | `ruff format --check .` |
| 静态检查 | `ruff check .` |
| 单元测试 | `pytest` |
| 覆盖率 | ≥ 80% (核心 ML 逻辑与预测函数) |
| 构建 | `docker build` 成功 |
| 模型指标 | 模型在测试集上 AUC ≥ 0.85 |

## 5. 不变约束

- 密钥、密码、私钥、Token **绝不写进代码或文档**,只进 GitHub Secrets / 环境变量。
- 数据集(`data/`)和模型产物(`artifacts/`)不进 Git,写进 `.gitignore`。
- `main` 分支受保护,日常开发必须走 feature 分支 + PR。
- CI 红灯不合并。
- CI 只做格式/测试/构建检查,不做 CD 自动部署。

## 6. 部署/CI 占位符取值

| 占位符 | 本项目取值 | 说明 |
|---|---|---|
| `<APP>` | `bank-marketing-app` | 应用名/镜像名/容器名 |
| `<DEPLOY_DIR>` | 不适用 | 本地部署,无需服务器目录 |
| `<PORT>` | `8004` | Streamlit 服务端口 |
| `<PYVER>` | `3.11` | Python 版本 |
| `<HEALTHCHECK>` | `/_stcore/health` | Streamlit 内置健康检查 |
| `<SSH_USER>` | 不适用 | 不做 CD,无需 SSH 用户 |
| `<SSH_HOST>` | 不适用 | 不做 CD,无需服务器地址 |

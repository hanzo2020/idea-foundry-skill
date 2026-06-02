# IdeaFoundry

[English](./README.md) | [中文](./README_zh.md)

一个用于从学术 PDF 中提炼“有理论依据、可复用的方法组件”的 Codex skill，并把结果维护到**单一累计 Markdown 组件库**中，方便后续做研究构思和方法组合。

## 文件说明

- `SKILL.md`：主技能说明文件，定义提炼规则与工作流。
- `templates/library_template.md`：累计组件库模板。
- `templates/component_card_template.md`：组件卡片模板。

## 建议安装位置

把整个 `idea-foundry` 文件夹复制到 Codex 的 skills 目录，例如：

```text
C:\Users\hanzo\.codex\skills\idea-foundry
```

复制完成后，**重启 Codex**。

## 这个 skill 适合做什么

IdeaFoundry 不是普通论文总结工具。它更适合做下面这类事：

- 从论文中提炼可复用的理论型组件
- 维护一个持续增长的 idea library
- 做跨论文去重，而不是每篇单独导出一份笔记
- 把方法抽象成以后还能重新组合的 research building blocks

它会优先关注这些更“可迁移”的内容：

- 数学 / 概率 / 统计基础
- 谱方法 / 几何方法 / 信息论方法
- 优化机制 / 分布建模机制
- 机制清楚的训练或推理策略
- 可复用的 loss / reweighting / calibration / abstention / optimization stabilizer

## 默认输出方式

默认维护**一个累计库文件**，而不是“每篇论文一个输出文件”。

默认文件名：

```text
idea_foundry_library.md
```

如果库已存在，就在原文件上更新；如果不存在，就按模板创建。

## 推荐命令

```text
Use the IdeaFoundry skill. Read all PDF papers in [folder path], extract theory-grounded method components, and update idea_foundry_library.md. Do not create one file per paper. Deduplicate similar components and update the indexes.
```

如果你希望同时维护中文版，也可以直接这样说：

```text
Use the IdeaFoundry skill. Read all PDF papers in [folder path], extract theory-grounded method components, update idea_foundry_library.md, and sync a Chinese version too. Do not create one file per paper. Deduplicate similar components and update the indexes.
```

## 使用提醒

- 这个 skill 更适合“建组件库”，不适合纯摘要式读论文。
- 如果论文理论抓手很弱，它可能只记 changelog，不强行建卡。
- 对相似机制，它会优先更新旧卡，而不是不断新建重复卡片。
- 适合批量读论文文件夹，也适合做第二轮 trick-focused 补抓。

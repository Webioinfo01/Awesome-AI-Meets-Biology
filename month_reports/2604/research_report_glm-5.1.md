# Research Paper Report for 2026-04-01:2026-04-30

## Overall Summary

This report covers 11 scientific papers published between April 1 and April 30, 2026, spanning four major categories: Reviews, AI Agents, Benchmarks, and Foundation Models. The research collectively demonstrates the accelerating convergence of large language models (LLMs), multi-agent architectures, and domain-specific biomedical applications, with a strong emphasis on clinical safety, multi-modal reasoning, and scalable data curation.

A prominent theme across the collection is the deployment of **multi-agent LLM systems** for specialized healthcare and biomedical tasks. Fan [1] provides a comprehensive systematic review and meta-analysis of AI agents in mental health, establishing a foundational understanding of the field's landscape. In ophthalmology, Sridhar [2] introduces an uncertainty-gated glaucoma screening approach that combines semi-supervised classification with multi-agent LLM deliberation, representing a novel fusion of traditional machine learning confidence estimation with agentic reasoning. Kassis [3] presents MetaMuse, a multi-agent system for biomedical metadata curation and harmonization, addressing the critical bottleneck of heterogeneous data management in biological research. Charney [4] tackles AI safety directly, demonstrating that an independent supervisory safety agent significantly improves LLM responses to expressions of suicidal ideation — a finding with immediate practical implications for mental health AI deployments.

The **benchmarks** category reveals growing scrutiny of LLM capabilities across diverse medical and biological domains. Onishi [5] evaluates LLM-based quality assurance tools for auto-contouring in medical imaging, while Zhang [6] benchmarks agentic LLMs on complex protein-set functional annotation tasks, pushing beyond simple classification into agentic multi-step reasoning. Skarżyński [7] asks whether multimodal LLMs can visually interpret auditory brainstem responses, probing the cross-modal reasoning limits of current models.

In **foundation models**, Powell [8] details a sophisticated multi-stage pipeline combining fine-tuned Bio-ClinicalBERT with LLM revision for extracting Age-Friendly 4M entities from nursing home text messages, achieving F1 improvements of +2 to +11 percentage points over prior methods while halving GPU memory requirements. Yao [9] introduces H2O, a foundation model bridging histopathology to spatial multi-omics profiling, representing a major step toward integrated multi-modal biomedical modeling. Chen [10] presents sdAbs-LLM for *de novo* antibody design with agentic evaluation, and Ben-Hur [11] contributes Deep-Plant, a supervised foundation model tailored for plant regulatory genomics.

Methodologically, the papers reflect a trend toward **hybrid architectures** that combine the strengths of specialized models (e.g., Bio-ClinicalBERT, domain-specific classifiers) with the flexibility of general-purpose LLMs for revision, reasoning, and error correction. The emphasis on open-source, locally deployable models [8] and safety-focused supervisory agents [4] signals growing attention to practical deployment constraints in clinical settings.

---

## Table of Contents

- [Reviews](#reviews)
- [AI Agents](#ai-agents)
- [Benchmarks](#benchmarks)
- [Foundation Models](#foundation-models)

---

## Reviews

### Category Summary

The Reviews category contains one significant contribution this month. Fan [1] conducts a systematic review and meta-analysis focused on artificial intelligence agents deployed in mental health contexts. This work is particularly timely given the concurrent publication of Charney [4] on safety agents for suicidal ideation response, making the review a valuable framing resource for interpreting emerging agentic safety architectures. Published in medRxiv, this review synthesizes evidence across multiple studies to evaluate the efficacy, safety, and methodological rigor of AI agents in mental health applications. The meta-analytic approach enables quantitative comparison across heterogeneous study designs, providing effect size estimates that individual studies cannot offer alone. This review serves as an important reference point for the broader collection, as several other papers in this report — particularly those in the AI Agents category — intersect with mental health and clinical safety considerations. The absence of specific methodological details in the available metadata suggests the review likely covers a broad spectrum of agent architectures, from simple chatbots to complex multi-agent deliberation systems, aligning with the technical diversity seen in the agentic systems presented by Sridhar [2], Kassis [3], and Charney [4].

| Index | Title | Domain | Venue | Team | DOI | Affiliation | Paper URL |
|-------|-------|--------|-------|------|-----|-------------|-----------|
| 1 | Artificial Intelligence Agents in Mental Health: A Systematic Review and Meta Analysis | Mental Health AI | medRxiv | L. Fan | 10.64898/2026.04.21.26351365 | — | [Link](https://www.semanticscholar.org/paper/fb326543d639565c4515d3ff2c61a5418c249418) |

---

## AI Agents

### Category Summary

The AI Agents category features three papers that collectively illustrate the breadth of multi-agent LLM applications in biomedicine, spanning clinical screening, data infrastructure, and patient safety.

Sridhar [2] introduces an **uncertainty-gated glaucoma screening** system that elegantly combines semi-supervised classification with multi-agent LLM deliberation. The key innovation lies in using model uncertainty as a gating mechanism — cases with high classification uncertainty are escalated to a multi-agent LLM deliberation panel, where multiple LLM agents debate and refine the diagnostic decision. This architecture optimizes computational resources by only engaging the expensive multi-agent deliberation for ambiguous cases, while confident classifications proceed directly. The ophthalmology domain demands high specificity to avoid unnecessary referrals, making the uncertainty-gating approach particularly well-suited.

Kassis [3] addresses a fundamentally different problem with MetaMuse, targeting **biomedical metadata curation and harmonization** — a critical but often overlooked bottleneck in large-scale biological research. Published in bioRxiv, MetaMuse deploys multiple specialized AI agents to handle different aspects of metadata processing, including ontology mapping, format standardization, and semantic reconciliation. While Sridhar [2] uses agents for diagnostic deliberation, Kassis [3] uses agents for data pipeline orchestration, demonstrating the versatility of multi-agent paradigms. The biology domain focus also highlights how agentic systems are extending beyond clinical medicine into foundational research infrastructure.

Charney [4] contributes a critical **AI safety** intervention, demonstrating that an independent supervisory safety agent improves LLM reactions to suicidal ideation. Unlike the domain-specific agents in [2] and [3], Charney's supervisory agent operates as an oversight layer that monitors and corrects the output of primary LLM systems when suicidal ideation is detected. This two-tier architecture — a primary conversational agent supervised by a dedicated safety agent — has direct implications for the mental health AI systems reviewed by Fan [1]. The medRxiv publication suggests clinical applicability, and the approach addresses a well-documented failure mode of unsupervised LLMs in mental health contexts.

| Index | Title | Domain | Venue | Team | DOI | Affiliation | Paper URL |
|-------|-------|--------|-------|------|-----|-------------|-----------|
| 2 | Uncertainty-Gated Glaucoma Screening: Combining Semi-Supervised Classification with Multi-Agent Large Language Model Deliberation | Ophthalmology | medRxiv | S. Sridhar | 10.64898/2026.04.17.26351127 | — | [Link](https://www.semanticscholar.org/paper/d23dbe77af51e1db22d66071a8bf8d1e6723686c) |
| 3 | MetaMuse: A Multi-Agent AI System for Biomedical Metadata Curation and Harmonization | Biomedical Metadata Curation | bioRxiv | T. Kassis | 10.64898/2026.04.12.718044 | — | [Link](https://www.semanticscholar.org/paper/5c414d15ca051b6ddd967c646f8c2f190b3efff8) |
| 4 | An independent supervisory safety agent improves reaction of large language models to suicidal ideation | AI Safety | medRxiv | A. Charney | 10.64898/2026.04.13.26350757 | — | [Link](https://www.semanticscholar.org/paper/18f8d02bb06ebe51c26dd69ceb1671bb3997254e) |

---

## Benchmarks

### Category Summary

The Benchmarks category includes three papers that rigorously evaluate LLM capabilities across medical imaging quality assurance, protein functional annotation, and audiological signal interpretation. These works collectively raise the bar for how LLM performance should be assessed in specialized scientific and clinical domains.

Onishi [5] evaluates an **LLM-based quality assurance tool for auto-contouring** in medical imaging. Auto-contouring is a critical step in radiation therapy planning, and quality assurance of these contours directly impacts patient safety. The benchmark evaluates how effectively LLMs can assess contour quality, identify errors, and flag cases requiring human review. Published in medRxiv, this work addresses the practical challenge of scaling QA processes in clinical settings where manual review of every contour is infeasible. The evaluation framework likely encompasses sensitivity and specificity metrics for error detection, as well as concordance with expert human reviewers.

Zhang [6] shifts the evaluation paradigm from passive assessment to **agentic benchmarking** for complex protein-set functional annotation. Unlike traditional benchmarks that evaluate single-step predictions, this work assesses agentic LLMs — models that can autonomously use tools, retrieve information, and iteratively refine their answers. The protein functional annotation domain requires integration of sequence analysis, literature knowledge, and ontology mapping, making it an ideal testbed for agentic capabilities. Published in bioRxiv, this benchmark pushes beyond the evaluation paradigm of Onishi [5] by requiring models to demonstrate multi-step reasoning and tool use rather than single-shot evaluation.

Skarżyński [7] poses a provocative cross-modal question: **can multimodal LLMs visually interpret auditory brainstem responses (ABRs)?** ABRs are traditionally interpreted from visual inspection of waveform plots by trained audiologists. This benchmark tests whether multimodal LLMs — trained on image-text pairs — can extract clinically meaningful information from ABR waveform images. The evaluation likely includes accuracy of wave identification (particularly Waves I, III, and V), threshold estimation, and diagnostic classification. The audiology domain is particularly challenging because it requires precise numerical reasoning from visual data — a capability that current multimodal LLMs may struggle with. This work complements Onishi [5] by extending LLM evaluation from medical imaging QA to physiological signal interpretation, while contrasting with Zhang [6] by testing visual reasoning rather than agentic tool use.

| Index | Title | Domain | Venue | Team | DOI | Affiliation | Paper URL |
|-------|-------|--------|-------|------|-----|-------------|-----------|
| 5 | Evaluating the Large Language Model-Based Quality Assurance Tool for Auto-Contouring | Medical Imaging | medRxiv | H. Onishi | 10.64898/2026.03.31.26349802 | — | [Link](https://www.semanticscholar.org/paper/2e87b3ca466314d6d7f66df1a15445a71c901c9e) |
| 6 | Benchmarking Agentic Large Language Models for Complex Protein-Set Functional Annotation | Protein Functional Annotation | bioRxiv | Xiaoyun Zhang | 10.64898/2026.04.18.719404 | — | [Link](https://www.semanticscholar.org/paper/ec05818f963451755cc7dd4e4e17c5866e341234) |
| 7 | Can Multimodal Large Language Models Visually Interpret Auditory Brainstem Responses? | Audiology | medRxiv | H. Skarżyński | 10.64898/2026.04.15.26350944 | — | [Link](https://www.semanticscholar.org/paper/3741a2854381c959e3d1ec4dee664a9a04d2178a) |

---

## Foundation Models

### Category Summary

The Foundation Models category is the largest in this report, featuring four papers that develop specialized foundation models spanning clinical NLP, spatial multi-omics, antibody design, and plant regulatory genomics. Together, these works demonstrate the trend toward domain-specific foundation models that combine pre-trained LLMs with task-specialized architectures.

Powell [8] provides the most methodologically detailed contribution in this collection, presenting a **multi-stage 4M Entity Recognition (4M-ER) pipeline** for extracting Age-Friendly Health Systems information (What Matters, Medication, Mentation, Mobility) from nursing home text messages. The pipeline combines a fine-tuned Bio-ClinicalBERT token classifier with LLM revision using open-source models (Gemma, Phi, Qwen, Mistral). Key technical innovations include: (1) a semantic similarity retriever for dynamic in-context exemplar selection, (2) restricting LLMs to revision only rather than end-to-end extraction, and (3) silver data augmentation for difficult domains. The pipeline achieves F1 improvements of +2 to +11 percentage points over a previously fine-tuned Gemma LLM across all 4M domains while using roughly half the GPU memory (12 vs 24 GB). Error analysis reveals that LLM revision reduces false positives by 25%–35% by resolving conversational ambiguity, while Bio-ClinicalBERT's high recall captures subtle entities. Silver data augmentation improves the hardest domains, raising What Matters F1 from 0.59 to 0.67 and Mobility from 0.64 to 0.67. The emphasis on locally deployed open-source models addresses critical data privacy constraints in clinical settings.

Yao [9] introduces **H2O**, a foundation model that bridges histopathology imaging to spatial multi-omics profiling. This work represents a significant advance in computational pathology by creating a unified model that can predict or integrate spatial multi-omics data (transcriptomics, proteomics, epigenomics) directly from standard histopathology images. While Powell [8] focuses on clinical NLP with text data, Yao [9] operates in the visual-omics space, highlighting the diversity of foundation model applications in biomedicine. The spatial multi-omics domain is particularly challenging due to the high dimensionality of omics data and the spatial relationships that must be preserved.

Chen [10] presents **sdAbs-LLM**, a generative large language model for *de novo* single-domain antibody design with integrated agentic evaluation. This work uniquely combines generative modeling with agentic self-assessment — the model not only designs antibody sequences but also employs agents to evaluate properties such as stability, binding affinity, and developability. The agentic evaluation component distinguishes this from traditional generative models and connects conceptually to the multi-agent deliberation approach of Sridhar [2]. Published in bioRxiv, sdAbs-LLM targets the biologically critical domain of therapeutic antibody engineering.

Ben-Hur [11] contributes **Deep-Plant**, a supervised foundation model specifically designed for plant regulatory genomics. This model addresses the challenge of understanding gene regulation in plant species, which requires capturing species-specific promoter elements, transcription factor binding sites, and regulatory motifs across diverse plant genomes. While Yao [9] and Chen [10] focus on human/animal biomedical applications, Ben-Hur [11] extends foundation model methodology to agricultural and botanical research. The supervised training approach contrasts with the self-supervised paradigm common in larger foundation models, reflecting the availability of curated regulatory annotations in plant genomics.

| Index | Title | Domain | Venue | Team | DOI | Affiliation | Paper URL |
|-------|-------|--------|-------|------|-----|-------------|-----------|
| 8 | Combining Token Classification With Large Language Model Revision for Age-Friendly 4M Entity Recognition From Nursing Home Text Messages: Development and Evaluation Study | Clinical NLP | medRxiv | K. Powell | 10.64898/2026.03.31.26349861 | — | [Link](https://www.semanticscholar.org/paper/1d09140bfaf8c33e54767f205a918dda11cc9db0) |
| 9 | H2O: A Foundation Model Bridging Histopathology to Spatial Multi-Omics Profiling | Spatial Multi-Omics | bioRxiv | Jianhua Yao | 10.64898/2026.04.21.717342 | — | [Link](https://www.semanticscholar.org/paper/8c1c4e2ffa9ba3156c782f95d8491c9dd4969f73) |
| 10 | sdAbs-LLM: Generative Large Language Models For de novo Antibody Design and Agentic Evaluation | Antibody Design | bioRxiv | J. Chen | 10.64898/2026.04.18.716776 | — | [Link](https://www.semanticscholar.org/paper/57f620be2b3b38e1471e7d94af210f3492759260) |
| 11 | Deep-Plant: a supervised foundation model for plant regulatory genomics | Plant Regulatory Genomics | bioRxiv | Asa Ben-Hur | 10.64898/2026.04.06.716755 | — | [Link](https://www.semanticscholar.org/paper/c9b0644c026380fb0e08cab42d1d686b2b8fb03f) |

---

**Report generated covering 11 papers across 4 categories for the period April 1–30, 2026.**
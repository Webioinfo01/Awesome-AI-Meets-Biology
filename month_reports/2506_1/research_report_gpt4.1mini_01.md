# Research Paper Report for 2025-06-01 to 2025-06-15

## Overall Summary

This collection of research papers from June 2025 spans a rich and diverse array of advancements primarily at the intersection of artificial intelligence (AI), biomedical sciences, molecular biology, and bioinformatics. A key overarching theme is the leveraging of large language models (LLMs) and agentic AI systems to automate, augment, and innovate biomedical research workflows, data analysis, and experimental design. For instance, Biomni [1] introduces a general-purpose biomedical AI agent that autonomously executes diverse research tasks by integrating LLM reasoning, retrieval-augmented planning, and code execution, thereby addressing the fragmented workflows that hamper biomedical discovery. Similarly, specialized agentic systems such as Cell-o1 [9] utilize reinforcement learning to enhance large language models’ reasoning capabilities for batch-level single-cell RNA annotation, showcasing significant improvement over standard LLM baselines.

These approaches exemplify a methodological advancement toward integrating domain-specific knowledge into AI agent architectures, which fuse data retrieval, reasoning, and autonomous experimental proposal, enabling interpretable and validated insights without task-specific prompt engineering [1,9]. The agentic paradigm is further explored by Agentomics-ML [6], which executes autonomous machine learning experiments on genomic and transcriptomic data through interaction with the file system and adaptive feedback loops, pushing forward the frontier of automated biomedical ML with reproducibility and iterative refinement.

Another prominent theme is the development of foundation models specialized for biological modalities. PixCell [11] pioneers a diffusion-based generative foundation model for histopathology images, overcoming data scarcity via self-supervised conditioning and enabling practical use cases like virtual staining and privacy-preserving data augmentation. Such multimodal and high-capacity models highlight a technical trend of merging generative and discriminative modeling tailored to biomedical imaging and omics data modalities.

Benchmarking and dataset curation receive critical attention, both in developing quantitative platforms and improving data quality. Protap [15] represents a comprehensive benchmarking effort evaluating protein modeling architectures, revealing that large-scale pretrained encoders do not always outperform supervised models fine-tuned on smaller sets, and that structural priors enhance specialized task performance. Securing dataset integrity is tackled via the concept of probably approximately correct labels [8], introducing mathematically grounded methods for trustworthy dataset curation using pretrained AI models that maintain error guarantees while reducing labeling cost.

The reports also engage with interdisciplinary concerns extending from biosecurity [12]—highlighting risks posed by AI foundation models enabling nefarious uses such as biological weapons development—to biostatistical methodology [14], calling for evolving statistical frameworks that integrate AI flexibility with traditional rigor to handle complex biomedical data. Bridging AI and human brain representations is examined through the lens of scale-invariance [13], revealing fundamental structural properties shared between neural and artificial embeddings and pointing toward deeper interpretability and evaluation frameworks.

Collectively, these papers demonstrate significant technical depth in combining LLM-based agents, generative models, reinforcement learning, and structured benchmarking to accelerate biomedical discovery and molecular biology, while acknowledging limitations such as dependence on training data diversity, challenges in generalization across heterogeneous datasets, and the need for robust evaluation and ethical frameworks. The convergence of these themes illustrates a maturing ecosystem where autonomous AI agents collaborate with human scientists to transform research productivity, healthcare applications, and biosecurity considerations [1,9,11,12].

---

## Table of Contents

- [AI Agents](#ai-agents)  
- [Foundation Models](#foundation-models)  
- [Reviews](#reviews)  
- [Benchmarks](#benchmarks)  

---

## AI Agents

The AI Agents category presents pioneering developments in autonomous systems designed to address complex biomedical and molecular tasks through agentic frameworks that combine large language models with domain adaptation and feedback-driven learning. Biomni [1] exemplifies a broad-spectrum biomedical AI agent capable of executing workflows across 25 biomedical domains by employing a foundational action discovery agent to construct a unified agentic environment. It skillfully integrates LLM reasoning, retrieval-augmented planning, and executable code without reliance on fixed templates, which enables strong task generalization in applications like causal gene prioritization and drug repurposing. This technical architecture marks a substantial leap in automating diverse biomedical research, validated through both benchmarks and real-world case studies of multimodal data interpretation.

Complementing this, Cell-o1 [9] targets a very specific yet challenging task: batch-level cell type annotation in single-cell RNA sequencing data. It distinguishes itself by training a 7B parameter LLM via supervised fine-tuning and reinforcement learning to reason across cellular batches, thus improving annotation accuracy by over 73% relative to previous models. This approach highlights the benefit of incorporating domain knowledge and reasoning traces in model training, demonstrating emergent expert-like capabilities.

Agentomics-ML [6] introduces a fully autonomous ML experimentation agent for genomic and transcriptomic datasets. By structuring the experimentation pipeline into iterative shell-based commands and integrating reflective feedback to adapt hyperparameters and model design, the system achieves competitive performance on benchmarks and narrows the gap with expert-crafted models. This methodical process of autonomous experimentation aids in reproducibility and scalable model deployment.

Other innovations include DeepSeq [4], which leverages agentic generative AI models augmented with real-time web search to automatically label high-throughput single-cell RNA sequencing data, achieving annotation accuracy up to 82.5%. This strategy reduces manual curation bottlenecks and facilitates the creation of virtual cell foundation models applicable for downstream perturbation prediction.

Curation and reliability of data labeling underpin successful AI applications, addressed by the Probably Approximately Correct Labels framework [7], which mathematically guarantees labeling accuracy with high probability, enhancing trust in automatically annotated datasets across domains like text, images, and protein folding.

Behavioral science aspects of AI agents are also explored [2], advocating for a scientific framework dedicated to studying AI agent behaviors in social and environmental contexts. This perspective enriches understanding of AI fairness, safety, and interpretability beyond internal mechanisms.

Finally, KODA [8] proposes an agentic system for antimicrobial drug target discovery in the gut microbiome, though details remain limited. Together, these works demonstrate a trend toward embedding domain expertise, reflection, and multi-step reasoning within autonomous agents, advancing technical sophistication and practical applicability in biomedical research.

| Index | Title                                                                                     | Domain                                                           | Venue                          | Team           | DOI                        | Affiliation                                     | paperUrl                                                                                      |
|-------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------|--------------------------------|----------------|----------------------------|------------------------------------------------|------------------------------------------------------------------------------------------------|
| 1     | Biomni: A General-Purpose Biomedical AI Agent                                           | Biomedical AI agent for autonomous research workflows            | bioRxiv                        | J. Leskovec    | 10.1101/2025.05.30.656746 | Stanford University                            | [Link](https://www.semanticscholar.org/paper/7bbe76e09d2aab075f006675355ebaa4020463a2)         |
| 2     | AI Agent Behavioral Science                                                             | Behavioral science of AI agents                                  | ArXiv                         | Yong Li        | 10.48550/arXiv.2506.06366 |                                                | [Link](https://www.semanticscholar.org/paper/e4bcb3f40c952a639c2bd665f8754defd67aad5e)          |
| 3     | Knowledge-guided Contextual Gene Set Analysis Using Large Language Models               | Context-aware gene set analysis using large language models     | ArXiv                         | Zhiyong Lu     | 10.48550/arXiv.2506.04303 |                                                | [Link](https://www.semanticscholar.org/paper/7cb3a28963a5ceb201e4092a4e52644c3436a7c7)          |
| 4     | DeepSeq: High-Throughput Single-Cell RNA Sequencing Data Labeling via Web Search-Augmented Agentic Generative AI Foundation Models | Agentic generative AI for single-cell RNA sequencing data labeling | bioRxiv                        | John R. Williams | 10.1101/2025.06.17.660107 | Department of Civil and Environmental Engineering, MIT | [Link](https://www.semanticscholar.org/paper/4d6ef2e715f81de2ce053c0c48f799c93e4d9309)          |
| 5     | Agentomics-ML: Autonomous Machine Learning Experimentation Agent for Genomic and Transcriptomic Data | Autonomous ML experimentation agent for genomic and transcriptomic data | ArXiv                         | Panagiotis Alexiou | 10.48550/arXiv.2506.05542 |                                                | [Link](https://www.semanticscholar.org/paper/f8666b034f4ddd25259d76c5c34e9fbb91dfc917)          |
| 6     | A User-Friendly Machine Learning Pipeline for Automated Leaf Segmentation in Atriplex lentiformis | Machine learning pipeline for automated leaf segmentation in plants | Bioinformatics and Biology Insights | Aikseng Ooi    | 10.1177/11779322251344033  |                                                | [Link](https://www.semanticscholar.org/paper/50cc21fce97d07dceb5021abb655ce9015a727f6)          |
| 7     | Probably Approximately Correct Labels                                                   | Method for dataset curation via probably approximately correct labels | ArXiv                         | Tijana Zrnic   | 10.48550/arXiv.2506.10908 |                                                | [Link](https://www.semanticscholar.org/paper/1cb28c5ca1eb9ebc3d29c0cf59fe4ef3fdd48fc6)          |
| 8     | KODA: An Agentic Framework for KEGG Orthology-Driven Discovery of Antimicrobial Drug Targets in Gut Microbiome | Agentic framework for antimicrobial drug target discovery in microbiome | bioRxiv                        | Mohammad R. K. Mofrad | 10.1101/2025.05.27.656480 | University of California Berkeley             | [Link](https://www.semanticscholar.org/paper/860d4b613b31bc64e81644015c0164627c67f31e)          |
| 9     | Cell-o1: Training LLMs to Solve Single-Cell Reasoning Puzzles with Reinforcement Learning | Training LLMs for batch-level single-cell RNA annotation via RL  | ArXiv                         | Zhiyong Lu     | 10.48550/arXiv.2506.02911 |                                                | [Link](https://www.semanticscholar.org/paper/5f145bd0636027e192d7c8d0102806166fc30d64)          |

---

## Foundation Models

This section highlights transformative efforts on large-scale and modality-specific foundation models tailored to biological contexts. PixCell [11] stands out as a diffusion-based generative foundation model for digital histopathology images trained on the expansive PanCan-30M dataset, consisting of over 69,000 histology whole-slide images covering multiple cancer types. The model employs progressive training combined with self-supervised conditioning that cushions the need for extensive annotations. This technical innovation allows PixCell to generate diverse, high-quality synthetic images usable for data augmentation, privacy-preserving data sharing, and educational applications.

A key architectural contribution is the mask-guided diffusion enabling targeted generation for specific cancer cell types, which significantly enhances performance in downstream tasks like cell segmentation. The practical implications include overcoming major barriers like scarcity of annotated histopathology data, coupled with regulatory accessibility advantages by using synthetic data. The public release of PixCell models fosters broader research adoption.

While only one paper populates this category, it provides a demonstration of how generative foundation models are advancing biological imaging with scalable architectures and training strategies that enable diversity and fidelity, addressing critical needs in computational pathology.

| Index | Title                                                   | Domain                                   | Venue | Team          | DOI                       | Affiliation | paperUrl                                                                                  |
|-------|---------------------------------------------------------|------------------------------------------|-------|---------------|---------------------------|-------------|------------------------------------------------------------------------------------------|
| 11    | PixCell: A generative foundation model for digital histopathology images | Generative foundation model for digital histopathology images | ArXiv | Dimitris Samaras | 10.48550/arXiv.2506.05127 |             | [Link](https://www.semanticscholar.org/paper/a4ac7f99debb0c757ba3f0f8291b24a4255d1d03)  |

---

## Reviews

The reviews provide critical and comprehensive overviews spanning AI's role in biological safety, plant molecular biology, agricultural breeding, and AI interpretability related to neuroscience and biostatistics.

McKelvey et al. [12] raise important biosecurity considerations, arguing that current AI foundation model safety assessments underestimate the risks of AI-enabled biological weapons development. They challenge assumptions around tacit knowledge, demonstrating that nonexperts have historically succeeded in complex technical tasks and that models like Llama 3.1 405B and ChatGPT-4o can guide pathogen synthesis. This analysis underscores the urgent need for refined benchmarks and governance.

Yan [13] reviews foundation models applied in plant molecular biology, tracing their progression from NLP-inspired systems to advanced models addressing plant-specific complexities — polyploidy, repetitive content, environment-responsive elements. Plant-tailored FMs such as GPN and AgroNT are evaluated alongside versatile universal models, noting challenges in data heterogeneity and computational efficiency. The paper calls for multi-modal integration and improved cross-species generalization.

Cao et al. [14] survey AI-assisted breeding efforts enhancing plant disease resistance, focusing on deep learning and large multi-modal models for detection, multi-omics analysis, and phenotype prediction. They highlight breakthroughs in CNN-based methods and emphasize future directions including federated learning integration for privacy and model robustness.

Liu et al. [15] explore scale-invariance as a fundamental principle connecting AI model embeddings with human brain neural representations. Using multi-scale analytical frameworks and fMRI alignment metrics, they find that embeddings exhibiting dimensional stability and structural similarity correlate better with brain data. Larger pretraining datasets and language modalities improve this property, suggesting a theoretical foundation bridging artificial and biological intelligence.

Lastly, Joshi [16] argues that traditional frequentist statistical methods require evolution to coexist with AI, advocating hybrid models combining rigor and AI flexibility. This integration is presented as key to advancing personalized medicine and public health, by enabling causal inference and decision-making on complex biomedical data.

Together, these reviews complement the empirical agentic and foundational model papers by situating current advances within critical ethical, computational, and theoretical contexts, highlighting opportunities and challenges for responsible and impactful AI deployment in biology.

| Index | Title                                                              | Domain                                   | Venue                             | Team          | DOI                           | Affiliation | paperUrl                                                                                   |
|-------|--------------------------------------------------------------------|------------------------------------------|----------------------------------|---------------|-------------------------------|-------------|-------------------------------------------------------------------------------------------|
| 12    | Contemporary AI foundation models increase biological weapons risk | Biosecurity risks posed by AI foundation models | ArXiv                           | T. G. McKelvey | 10.48550/arXiv.2506.13798     |             | [Link](https://www.semanticscholar.org/paper/e4854e4c12a3dc1964775c7368b3ee3adb02982e)    |
| 13    | Foundation models in plant molecular biology: advances, challenges, and future directions | Foundation models in plant molecular biology | Frontiers in Plant Science        | Jun Yan       | 10.3389/fpls.2025.1611992     |             | [Link](https://www.semanticscholar.org/paper/98b561595f5bf7d47456b83d5f52af31ebf0e9ae)    |
| 14    | Artificial Intelligence-Assisted Breeding for Plant Disease Resistance | AI-assisted breeding for plant disease resistance | International Journal of Molecular Sciences | Yanyong Cao   | 10.3390/ijms26115324           |             | [Link](https://www.semanticscholar.org/paper/74d45591664632d4150df72d6b5adb2b7b65e267)    |
| 15    | Scale-Invariance Drives Convergence in AI and Brain Representations | Scale-invariance in AI and brain representations | ArXiv                           | Quanying Liu  | 10.48550/arXiv.2506.12117     |             | [Link](https://www.semanticscholar.org/paper/3a01165637266c9da59be95a4a0a78f37af2b6dc)    |
| 16    | Why Traditional Statistical Methods Need to Evolve in the Age of Artificial Intelligence: A Biostatistical Perspective | Integration of AI and traditional biostatistics | Nepal Journal of Public Health     | Deepak Raj Joshi | 10.70280/njph(2025)v2i1.31    |             | [Link](https://www.semanticscholar.org/paper/0ee50fdccfabf9204c91cf4238e08f3035794adf)     |

---

## Benchmarks

The single paper in this section, Protap [17], establishes a rigorous benchmark suite targeting protein modeling applications with an emphasis on realistic downstream tasks. It compares a variety of backbone model architectures, pretraining approaches (e.g., large-scale unsupervised vs. supervised learning), and domain-specific biological priors across five tasks including enzyme-catalyzed cleavage site prediction and targeted protein degradation.

Key empirical findings indicate that over-reliance on large-scale pretrained encoders is premature; supervised encoders trained on smaller, task-specific datasets sometimes outperform them. Incorporating structural information during fine-tuning consistently yields strong results. Protap’s contribution lies in advancing evaluation standards that combine biological relevance, domain specificity, and modeling granularity, thereby informing model selection and future architectural choices for protein informatics.

| Index | Title                                                       | Domain                                             | Venue | Team          | DOI                        | Affiliation | paperUrl                                                                                   |
|-------|-------------------------------------------------------------|----------------------------------------------------|-------|---------------|----------------------------|-------------|-------------------------------------------------------------------------------------------|
| 17    | Protap: A Benchmark for Protein Modeling on Realistic Downstream Applications | Benchmarking protein modeling architectures and pretraining strategies | ArXiv | Enyan Dai     | 10.48550/arXiv.2506.02052 |             | [Link](https://www.semanticscholar.org/paper/5f65dfc5038c92492af55364ada876303e247be8)    |

---

This report captures nuanced trends in leveraging agentic systems, generative and discriminative foundation models, rigorous benchmarking, and thoughtful ethical and biological reviews toward accelerating biomedical research through AI in June 2025 publications.
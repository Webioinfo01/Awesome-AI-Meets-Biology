# Research Paper Report for 2025-12-15:2025-12-31

## Overall Summary

The research landscape between December 15 and December 31, 2025, showcases a profound and accelerating integration of Large Language Models (LLMs) and specialized foundation models into the biomedical, clinical, and material sciences. A prominent theme is the development of domain-specific foundation models [1], [3], [4] and the enhancement of multimodal architectures [2]. For instance, models like mRNA-GPT [1] and GenBrain [3] push the boundaries of generative biology and neuroimaging. Concurrently, UPATHLN [4] introduces critical uncertainty quantification for pan-cancer pathology, achieving an impressive 0.986 AUC and 100% conditional sensitivity by acting as a fail-safe against overconfident AI errors.

Benchmarking efforts rigorously evaluate LLMs against traditional machine learning and physician standards, proving their readiness for clinical deployment. In diabetes management, GPT-4.1 and LLaMA models demonstrated superior glucose forecasting capabilities compared to traditional deep learning models like LSTMs, while also offering natural language interpretability [5]. Similarly, GPT-5 outperformed both algorithmic models and earlier LLM iterations in assigning causes of death from verbal autopsies, achieving high concordance with physician coding across diverse age groups [6].

Practical applications of LLMs are expanding into complex data extraction and reasoning tasks. Researchers are combining LLMs with text mining for toxicology to map pregnancy complications [8] and utilizing human-AI-curated few-shot learning for material synthesis extraction [9]. Furthermore, augmenting LLMs with epidemiological knowledge graphs (GRAG) has proven highly effective in reconstructing life-course risk pathways, such as the link between gestational diabetes and dementia, significantly reducing AI confabulation [10]. Systematic reviews also highlight the growing footprint of LLMs in specific clinical domains like obesity management [7].

To support these advanced models, comprehensive databases like DRPMKB 1.0 [11] are being developed to standardize and personalize AI-driven drug repositioning. Finally, the emergence of autonomous AI agents marks a significant leap forward. Agents are being deployed for zoonotic surveillance [12], pathogen discovery [13], and patient safety, where tools like SAFE-AI use ontology-driven rules to minimize hallucinations in detecting medication errors [14]. Concurrently, the biosecurity implications of these powerful models are being addressed by agentic risk auditing frameworks like SAGE, which evaluate the adversarial vulnerabilities of genomic foundation models [15]. Together, these 15 papers illustrate a clear trajectory toward more reliable, interpretable, and agentic AI systems in scientific research.

## Table of Contents
* [Foundation Models](#foundation-models)
* [Benchmarks](#benchmarks)
* [Reviews](#reviews)
* [Applications](#applications)
* [Databases](#databases)
* [AI Agents](#ai-agents)

## Foundation Models

The foundation models category highlights a dual focus on domain-specific generative capabilities and architectural improvements for multimodal understanding. Papers [1] and [3] introduce highly specialized generative models: mRNA-GPT [1] targets efficient coding sequence generation in biology, while GenBrain [3] focuses on multimodal brain imaging. These models represent the frontier of generative AI applied directly to complex biological and physiological data. In contrast, [2] addresses the architectural limitations of general Multi-Modal Large Language Models (MLLMs). By introducing vMLLM, which utilizes a Multi-level Aggregation Module (MAM) and an Intra- and inter-modal Enhancement Module (IEM), the authors successfully extract and amplify task-relevant visual features, significantly boosting performance across diverse benchmarks. 

While [1], [2], and [3] focus on generation and feature enhancement, [4] tackles a critical limitation in clinical AI: safety and reliability. UPATHLN [4] is a pathology foundation model designed for pan-cancer lymph node metastasis assessment. It improves upon standard predictive models by decoupling uncertainty estimation from the primary prediction. This uncertainty module acts as a mandatory fail-safe, flagging potential false negatives for human review. As a result, it achieved 100% conditional sensitivity and reduced the review burden on negative lymph nodes by 73.2%. This comparative shift from purely maximizing accuracy to explicitly modeling uncertainty sets a new benchmark for safety-critical AI in medicine.

| Index | Title | Domain | Venue | Team | DOI | Affiliation | paperUrl |
|---|---|---|---|---|---|---|---|
| 1 | Large generative mRNA language foundation model for efficient coding sequence generation and design with mRNA-GPT | mRNA sequence generation | bioRxiv | {'name': 'Yutaka Saito'} | 10.64898/2025.12.22.695962 | Not Provided | [Link](https://www.semanticscholar.org/paper/7e61e5a7b3605c8a5413c0453edaaa65055f563d) |
| 2 | Boosting Multi-Modal Large Language Model With Enhanced Visual Features | Multimodal LLMs | IEEE Transactions on Pattern Analysis and Machine Intelligence | {'name': 'Rongrong Ji'} | 10.1109/TPAMI.2025.3644851 | Not Provided | [Link](https://www.semanticscholar.org/paper/27ac6547fed9ed9ac4f82b06bde4fd853aaad2e7) |
| 3 | GenBrain: A Generative Foundation Model of Multimodal Brain Imaging | Brain Imaging | medRxiv | {'name': 'W. Gong'} | 10.64898/2025.12.19.25342614 | Not Provided | [Link](https://www.semanticscholar.org/paper/270987463346ea5b85fb6b4f0745a27e9c22ec3e) |
| 4 | High-sensitivity pan-cancer AI assessment of lymph node metastasis via uncertainty quantification | Pathology | medRxiv | {'name': 'Guanzhen Yu'} | 10.1038/s41746-026-02564-y | Not Provided | [Link](https://www.semanticscholar.org/paper/adec35d82936a1582fae1e604fb9aa709652be87) |

## Benchmarks

Benchmarking studies in this period rigorously evaluate the performance of LLMs against traditional machine learning models and human expert standards in clinical settings. Paper [5] focuses on time-series forecasting for Type 2 Diabetes management, comparing traditional models (XGBoost), deep learning (LSTM), and fine-tuned LLMs (GPT-4.1, LLaMA) for predicting glucose levels. The study found that GPT-4.1 excelled at 30- and 60-minute forecasting horizons, while LLaMA-7B performed best at 90 minutes. Crucially, [5] highlights that LLMs provide natural language interpretability that aligns perfectly with traditional Explainable AI (XAI) techniques, identifying recent glucose readings as key predictors.

In contrast, [6] evaluates LLMs on a complex narrative classification task: assigning causes of death from verbal autopsies in Sierra Leone. Comparing GPT-3.5, GPT-4, and GPT-5 against symptom-based algorithms (InterVA-5, InSilicoVA) and physician coding, the study demonstrates a clear evolutionary leap in LLM capabilities. GPT-5 emerged as the superior model with a partial chance-corrected concordance (PCCC) of 0.71, significantly outperforming older LLMs and traditional algorithms across adult, child, and neonatal deaths. While [5] proves the efficacy of LLMs in numerical time-series forecasting, [6] validates their superior natural language understanding in epidemiological surveillance, both underscoring the increasing viability of LLMs to match or exceed specialized clinical baselines.

| Index | Title | Domain | Venue | Team | DOI | Affiliation | paperUrl |
|---|---|---|---|---|---|---|---|
| 5 | Interpretable glucose forecasting for type 2 diabetes across traditional, deep, and large language models | Diabetes Management | Scientific Reports | {'name': 'Hind Almisbahi'} | 10.1038/s41598-025-32373-4 | Not Provided | [Link](https://www.semanticscholar.org/paper/dcfa2e2cc3260aa02d6594f8c463efc3e755e78c) |
| 6 | Computer assisted verbal autopsy: comparing large language models to physicians for assigning causes to 6939 deaths in Sierra Leone from 2019–2022 | Public Health | BMC Medicine | {'name': 'R. Ansumana'} | 10.1186/s12916-025-04584-z | Not Provided | [Link](https://www.semanticscholar.org/paper/fb7ddfa2773f0dab97cda7e860153c2c368d69c4) |

## Reviews

Systematic reviews are essential for synthesizing the rapid influx of AI research within specific medical domains, providing a consolidated view of current capabilities and limitations. Paper [7] offers a comprehensive systematic review of Large Language Models applied to the field of obesity. Published in the highly regarded *International Journal of Obesity*, this review aggregates the fragmented literature surrounding the use of conversational AI and predictive language models in metabolic health. 

Although the specific abstract details are omitted, the context of the publication suggests a thorough examination of how LLMs are being utilized for patient education, dietary tracking, personalized weight management interventions, and the analysis of epidemiological data related to obesity. By synthesizing findings from various primary studies, [7] serves as a foundational reference point for clinicians and researchers. It likely highlights both the potential benefits—such as scalable, personalized patient interactions—and the current limitations, including the risks of hallucination or the lack of deep, personalized clinical context when deploying LLMs for chronic disease management.

| Index | Title | Domain | Venue | Team | DOI | Affiliation | paperUrl |
|---|---|---|---|---|---|---|---|
| 7 | Large language models in obesity: a systematic review. | Obesity | International Journal of Obesity | {'name': 'N. Kulthamrongsri'} | 10.1038/s41366-025-01992-2 | Not Provided | [Link](https://www.semanticscholar.org/paper/8f60d9556711df62a20f9890ddef77f8dafcf7b0) |

## Applications

The applications category demonstrates the transformative power of LLMs in extracting, synthesizing, and reasoning over complex scientific data. Paper [8] combines suspect screening with LLM-based text mining to characterize organic compounds in human milk, successfully identifying novel compounds linked to pregnancy complications like gestational hypertension and diabetes. Similarly, [9] introduces MaterialBrain, a pipeline that uses human-AI-curated few-shot LLMs to extract metal-organic framework (MOF) synthesis routes from literature. MaterialBrain significantly outperforms zero-shot baselines, guiding the synthesis of materials that surpass 99.2% of reported MOFs in specific surface area.

While [8] and [9] focus on chemical and material data extraction from massive literature corpora, [10] tackles complex reasoning in epidemiology. It augments GPT-4 with a causal knowledge graph using Graph Retrieval-Augmented Generation (GRAG) to reconstruct life-course risk pathways between gestational diabetes and dementia. This structured approach using semantic triples drastically reduces LLM confabulation and successfully identified 108 maternal candidate mediators. However, [10] also notes a critical limitation: LLMs tend to overestimate clinical relevance, necessitating human-AI collaboration. Together, these papers showcase LLMs transitioning from passive text processors to active engines of scientific discovery and hypothesis generation.

| Index | Title | Domain | Venue | Team | DOI | Affiliation | paperUrl |
|---|---|---|---|---|---|---|---|
| 8 | Combining Suspect Screening with Large Language Model-Based Text Mining to Comprehensively Characterize Organic Compounds in Human Milk Associated with Pregnancy Complications. | Toxicology | Environmental Science and Technology | {'name': 'Minghui Zheng'} | 10.1021/acs.est.5c12937 | Not Provided | [Link](https://www.semanticscholar.org/paper/d76e366b4c6df88dfd0e5e37d18260b09815e375) |
| 9 | MaterialBrain: High-Performance Material Synthesis Extraction via Human-AI-Curated Few-Shot Large Language Models | Materials Science | Journal of Chemical Information and Modeling | {'name': 'Ge Wang'} | 10.1021/acs.jcim.5c02299 | Not Provided | [Link](https://www.semanticscholar.org/paper/c1e2d1b164d639f803c46ae335371e8ff9f66eb8) |
| 10 | Knowledge graph-augmented large language models for reconstructing life course risk pathways: a gestational diabetes mellitus-to-dementia case study | Epidemiology | J. Am. Medical Informatics Assoc. | {'name': 'Jian Du'} | 10.1093/jamia/ocaf219 | Not Provided | [Link](https://www.semanticscholar.org/paper/32fca5a9a276a00ec8c2ac5c46309a69c0ceb223) |

## Databases

The rapid proliferation of AI models in biomedicine necessitates structured, high-quality databases to organize, evaluate, and deploy them effectively. Paper [11] addresses this need by introducing DRPMKB 1.0, a comprehensive, AI-oriented knowledge base specifically designed for drug repositioning prediction models. The platform tackles the fragmentation of computational models by compiling extensive data from PubMed, encompassing 45 categories, 193 models, and 693 data entries. 

Unlike standard biological databases that merely store molecular interactions or chemical structures, DRPMKB 1.0 establishes a unique dual-evaluation framework. This framework appraises both the inherent quality of the computational models and the evidentiary support for their predictions. By integrating diverse data and models, DRPMKB 1.0 offers tailored model recommendations based on user-specific data, thereby significantly improving prediction accuracy for drug repositioning tasks. Furthermore, it provides a robust foundation for developers to seamlessly integrate new datasets and continuously refine models. This database bridges the critical gap between raw computational power and practical, personalized pharmacological applications, ensuring that LLMs and other AI models have access to curated, task-specific knowledge.

| Index | Title | Domain | Venue | Team | DOI | Affiliation | paperUrl |
|---|---|---|---|---|---|---|---|
| 11 | DRPMKB1.0: A Comprehensive Knowledge Base for an AI-Oriented Drug Repositioning Prediction Model | Drug Repositioning | Journal of Chemical Information and Modeling | {'name': 'Bairong Shen'} | 10.1021/acs.jcim.5c01945 | Not Provided | [Link](https://www.semanticscholar.org/paper/32d3cb0da0e5ad703eb29a90047efa53156a199c) |

## AI Agents

The shift from static, prompt-response models to autonomous AI agents is a defining trend in this period's research. Papers [12] and [13] introduce specialized biological agents: VirSentAI [12] is designed for automated zoonotic surveillance and drug repurposing, while the Moremi Bio Agent [13] focuses on pathogen and antigen discovery using Neisseria meningitidis reference data. These agents represent a move toward continuous, automated biological monitoring and discovery.

In the clinical realm, [14] presents SAFE-AI, a medically grounded LLM agent that detects patient safety events, such as epinephrine overdoses, with 97.9% accuracy. SAFE-AI improves upon baseline LLMs by using strict, ontology-driven rules to minimize hallucinations, addressing the critical limitation of over-reliance on probabilistic pattern recognition in high-stakes medical scenarios. Conversely, [15] addresses the security risks inherent in deploying such powerful models. It introduces SAGE, an agentic framework that audits adversarial vulnerabilities in Genomic Foundation Models (GFMs) like ESM2. SAGE uses soft prompt perturbations to reveal that even state-of-the-art GFMs are sensitive to targeted attacks, causing measurable performance degradation. Together, these papers illustrate the dual imperative of deploying highly capable AI agents [12, 13, 14] while rigorously auditing their safety and biosecurity robustness [15].

| Index | Title | Domain | Venue | Team | DOI | Affiliation | paperUrl |
|---|---|---|---|---|---|---|---|
| 12 | Viral Sentry AI (VirSentAI) - Automated Zoonotic Surveillance & Drug Repurposing Agent | Zoonotic Surveillance | bioRxiv | {'name': 'Eduardo Tejera'} | 10.64898/2025.12.29.684576 | Not Provided | [Link](https://www.semanticscholar.org/paper/418f1dbe4d9e45cfc7a2e0688c20d81fcb8c2de9) |
| 13 | Moremi Bio Agent: Using Neisseria meningitidis Reference Data For The Double Blinded Validation of A General Purpose Biology-Trained Reasoning Model for Pathogen and Antigen Discovery | Pathogen Discovery | bioRxiv | {'name': 'D. Akogo'} | 10.64898/2025.12.17.694980 | Not Provided | [Link](https://www.semanticscholar.org/paper/21e8c7b8e04f3a1e3c3ccc8ccdf285eb608c3a44) |
| 14 | A medically grounded LLM agent–based tool to detect patient safety events in medical records | Patient Safety | medRxiv | {'name': 'J. Guise'} | 10.64898/2025.12.16.25342438 | Not Provided | [Link](https://www.semanticscholar.org/paper/e2c588ab5ffec9297c68b62d1792285b4fc5dd01) |
| 15 | Biosecurity-Aware AI: Agentic Risk Auditing of Soft Prompt Attacks on ESM-Based Variant Predictors | Biosecurity | arXiv.org | {'name': 'Huixin Zhan'} | 10.48550/arXiv.2512.17146 | Not Provided | [Link](https://www.semanticscholar.org/paper/82be906a8aa6895796b2b9afc42953dd3ae2392e) |
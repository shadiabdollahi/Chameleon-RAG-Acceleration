# Chameleon-RAG-Acceleration

Repository for our VLDB'25 paper **[Chameleon: A Heterogeneous and Disaggregated Accelerator System for Retrieval-Augmented Language Models](https://arxiv.org/pdf/2310.09949)**

Chameleon is a heterogeneous accelerator system for RAG serving. It prototypes FPGA-based accelerators for retrieval and GPU-based LLM inference.

## 🎓 Citing Chameleon

```
@article{jiang2023chameleon,
  title={Chameleon: a heterogeneous and disaggregated accelerator system for retrieval-augmented language models},
  author={Jiang, Wenqi and Zeller, Marco and Waleffe, Roger and Hoefler, Torsten and Alonso, Gustavo},
  journal={Proceedings of the VLDB Endowment},
  year={2025}
}

@inproceedings{jiang2023co,
  title={Co-design hardware and algorithm for vector search},
  author={Jiang, Wenqi and Li, Shigang and Zhu, Yu and de Fine Licht, Johannes and He, Zhenhao and Shi, Runbin and Renggli, Cedric and Zhang, Shuai and Rekatsinas, Theodoros and Hoefler, Torsten and others},
  booktitle={Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis},
  pages={1--15},
  year={2023}
}
```

## Related Projects

### ISCA'25: [RAGO: Systematic Performance Optimization for Retrieval-Augmented Generation Serving](https://arxiv.org/pdf/2503.14649). 

System Performance Optimization for RAG.

Code: https://github.com/google/rago 

```
@inproceedings{rago:isca:2025,
  title={RAGO: Systematic Performance Optimization for Retrieval-Augmented Generation Serving},
  author={Jiang, Wenqi and Subramanian, Suvinay and Graves, Cat and Alonso, Gustavo and Yazdanbakhsh, Amir and Dadu, Vidushi},
  booktitle = {Proceedings of the 52th Annual International Symposium on Computer Architecture}
  year={2025}
}
```

### KDD'25 [PipeRAG: Fast retrieval-augmented generation via adaptive pipeline parallelism](https://www.amazon.science/publications/piperag-fast-retrieval-augmented-generation-via-adaptive-pipeline-parallelism)

Efficient algorithm for iterative RAG. 

Code: https://github.com/amazon-science/piperag 

```
@article{jiang2025piperag,
  title={PipeRAG: Fast retrieval-augmented generation via adaptive pipeline parallelism},
  author={Jiang, Wenqi and Zhang, Shuai and Han, Boran and Wang, Jie and Wang, Yuyang Bernie and Kraska, Tim},
  journal={Proceedings of the 31th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},
  year={2025}
}
```

### SC'23 [Co-design Hardware and Algorithm for Vector Search](https://arxiv.org/pdf/2306.11182)

Accelerating product-quantization-based vector search. 

Code: https://github.com/WenqiJiang/SC-ANN-FPGA

```
@inproceedings{jiang2023co,
  title={Co-design hardware and algorithm for vector search},
  author={Jiang, Wenqi and Li, Shigang and Zhu, Yu and de Fine Licht, Johannes and He, Zhenhao and Shi, Runbin and Renggli, Cedric and Zhang, Shuai and Rekatsinas, Theodoros and Hoefler, Torsten and others},
  booktitle={Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis},
  pages={1--15},
  year={2023}
}
```

### VLDB'25 [Fast Graph Vector Search via Hardware Acceleration and Delayed-Synchronization Traversal](https://arxiv.org/abs/2406.12385)

Accelerating graph-based vector search.

Code: https://github.com/fpgasystems/Falcon-accelerate-graph-vector-search

```
@article{jiang2024accelerating,
  title={Accelerating Graph-based Vector Search via Delayed-Synchronization Traversal},
  author={Jiang, Wenqi and Hu, Hang and Hoefler, Torsten and Alonso, Gustavo},
  journal={arXiv preprint arXiv:2406.12385},
  year={2024}
}
```

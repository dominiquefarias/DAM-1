ollama list

dominique@MacBook-Pro-Dominique:~$ ollama list
NAME                ID              SIZE      MODIFIED    
qwen2.5-coder:7b    dae161e27b0e    4.7 GB    12 days ago    
dominique@MacBook-Pro-Dominique:~$

ollama run qwen2.5-coder:7b "crea una web en HTML, sin comentarios, solo el código"

dominique@MacBook-Pro-Dominique:~$ ollama run qwen2.5-coder:7b "crea un programa en Python, que sume 4+3. Solo quiero el codigo, ningun comentario."

```python
print(4 + 3)
```

# ex02 — load_image.py

## O que o exercício pede

Escrever uma função `ft_load(path)` que:

1. **Carrega uma imagem** do disco dado um caminho (`path`)
2. **Imprime o shape** da imagem (ex: `The shape of image is: (257, 450, 3)`)
3. **Imprime o array** da imagem (os dados numéricos em si)
4. **Retorna o array** como `np.ndarray`
5. **Trata erro** se o caminho não existir (`FileNotFoundError`)

---

## Conceitos que você precisa saber

### 1. NumPy arrays e shape
Você já usou isso no ex00 e ex01:
- Uma imagem é um array 3D: `(altura, largura, canais_de_cor)`
- Ex: `(257, 450, 3)` → 257 linhas, 450 colunas, 3 canais (RGB)
- `.shape` → tupla com as dimensões

### 2. `np.ndarray` como type hint
No ex01 você usou `list` como tipo de retorno. Aqui o tipo correto é `np.ndarray` (não `array` que não existe solto).

### 3. `matplotlib.image.imread`
Novidade deste exercício. É o que carrega a imagem do disco como array numpy:
```python
from matplotlib import image as mpimg
img = mpimg.imread("caminho/imagem.jpg")  # retorna np.ndarray
```

### 4. `os.path.exists`
Para verificar se o arquivo existe antes de tentar abrir:
```python
import os
if not os.path.exists(path):
    raise FileNotFoundError(...)
```

---

## O que falta no seu código atual

| Problema | O que está | O que deveria ser |
|---|---|---|
| Type hint errado | `-> array` | `-> np.ndarray` |
| Não retorna nada | sem `return` | `return img` |
| Não imprime o array | só imprime shape | `print(img)` também |
| Sem tratamento de erro | nada | `FileNotFoundError` se path inválido |
| Falta `import os` | não importado | necessário pro `os.path.exists` |

**Sintoma visível agora:** rodar o tester imprime `None` porque a função não retorna nada.

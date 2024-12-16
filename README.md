## PD29S Atividade 3
### Integrantes
- Roberto Goz | 2372665
- João Cervino | 2372576


### Apresentação do Código de Troca de Rostos

Este código implementa um processo de troca de rostos em imagens utilizando a biblioteca OpenCV. Ele combina várias técnicas de processamento de imagem, como triangulação de Delaunay, transformação afim e clonagem contínua para realizar uma troca realista de regiões faciais entre duas imagens. Abaixo, os principais componentes e etapas do código são explicados.

---

#### **1. Funções Auxiliares**

- **`readPoints(path)`**
  - Lê coordenadas de pontos armazenadas em um arquivo texto.
  - **Objetivo:** Fornecer os pontos faciais necessários para as transformações geométricas.
  - **Exemplo de entrada/saída:** Um arquivo contendo pontos no formato `x y`, retorna uma lista de tuplas `[(x1, y1), (x2, y2), ...]`.

- **`applyAffineTransform(src, srcTri, dstTri, size)`**
  - Aplica uma transformação afim que mapeia um triângulo da imagem de origem (`srcTri`) para um triângulo na imagem de destino (`dstTri`).
  - **Objetivo:** Ajustar a região triangular de uma imagem para se alinhar com outra.

- **`rectContains(rect, point)`**
  - Verifica se um ponto está dentro de um retângulo definido por `(x, y, w, h)`.
  - **Objetivo:** Validar triângulos para a triangulação de Delaunay.

- **`calculateDelaunayTriangles(rect, points)`**
  - Calcula a triangulação de Delaunay para um conjunto de pontos dentro de um retângulo.
  - **Objetivo:** Dividir a área delimitada em triângulos que serão usados para a transformação.

- **`warpTriangle(img1, img2, t1, t2)`**
  - Alinha um triângulo de `img1` (definido por `t1`) com um triângulo correspondente de `img2` (definido por `t2`) e mescla a transformação em `img2`.
  - **Objetivo:** Realizar ajustes triangulares locais para mapear rostos.

---

#### **2. Lógica Principal do Script**

1. **Verificação de Versão do OpenCV**
   - Certifica-se de que a versão instalada suporta as operações usadas no código (>= OpenCV 3.0).

2. **Leitura de Arquivos**
   - Duas imagens (`boy.jpg` e `rob.jpg`) são carregadas.
   - Arquivos correspondentes (`boy.jpg.txt` e `rob.jpg.txt`) contêm pontos de controle faciais.

3. **Cálculo do Envoltório Convexo**
   - O `convexHull` é calculado para alinhar as características faciais de ambas as imagens.

4. **Triangulação e Transformação**
   - Utiliza triangulação de Delaunay nos pontos do envoltório convexo da segunda imagem.
   - Cada triângulo é transformado e mapeado para a posição correspondente na imagem de destino.

5. **Criação de Máscara e Clonagem**
   - Uma máscara é criada para limitar a área do rosto transformado.
   - Utiliza clonagem contínua (seamlessClone) para integrar o rosto transformado na imagem de destino, garantindo transições suaves.

---

#### **3. Fluxo Visual**

1. **Entrada:**
   - Imagem de origem: `boy.jpg`
   - Imagem de destino: `rob.jpg`
   - Pontos faciais: Arquivos `.txt`

2. **Processamento:**
   - Detecção de pontos faciais.
   - Alinhamento geométrico via triangulação de Delaunay.
   - Mapeamento triangular e mesclagem local.

3. **Saída:**
   - Imagem combinada com o rosto trocado exibida em uma janela com o título `"Face Swapped"`.

---

#### **4. Observações Finais**

- **Requisitos de Entrada:**
  - As imagens devem ter arquivos `.txt` associados com coordenadas faciais correspondentes.
  - A estrutura dos pontos precisa ser consistente entre as imagens.

- **Benefícios:**
  - Usa técnicas avançadas de processamento de imagem para produzir resultados realistas.
  - Modularidade das funções facilita a personalização e extensibilidade.

- **Limitações:**
  - Depende fortemente da qualidade dos pontos faciais fornecidos.
  - Pode apresentar artefatos visuais em casos de grandes diferenças entre as imagens.

Se precisar de mais detalhes ou visualizações sobre o funcionamento do código, estou à disposição!

# Cálculo de Transferência de Calor em Aleta Triangular

## 📋 Descrição

Este projeto realiza a análise térmica de uma **aleta triangular** utilizando funções de Bessel modificadas. O programa calcula:

- **Eficiência da aleta (η)**: Razão entre o calor real dissipado e o calor máximo possível
- **Efetividade da aleta (ε)**: Razão entre o calor dissipado e o calor que seria dissipado sem a aleta
- **Calor dissipado por unidade de largura (q')**: Potência térmica em W/m
- **Perfil de temperatura**: Gráfico da distribuição de temperatura ao longo da aleta (análise similar a elementos finitos)

## 🚀 Características

✅ Entrada manual de dados interativa  
✅ Valores padrão automáticos  
✅ Gráficos de perfil de temperatura em alta resolução  
✅ Análise baseada em teoria clássica de aletas triangulares  

## 📦 Dependências

O script requer as seguintes bibliotecas Python:

| Biblioteca | Versão | Descrição |
|-----------|--------|-----------|
| `numpy` | ≥ 1.20 | Computação numérica |
| `scipy` | ≥ 1.7 | Funções especiais (Bessel) |
| `matplotlib` | ≥ 3.4 | Visualização e gráficos |

## 💻 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/sandroeng23/Calculo-de-transferencia-de-calor-em-aleta-triangular.git
cd Calculo-de-transferencia-de-calor-em-aleta-triangular
```

### 2. Crie um ambiente virtual (recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install numpy scipy matplotlib
```

**Ou use o arquivo requirements.txt (se disponível):**

```bash
pip install -r requirements.txt
```

## ▶️ Como Usar

### Executar o script

```bash
python aletatriangular.py
```

### Entrada de dados

O programa solicita os seguintes parâmetros (com valores padrão entre colchetes):

```
Temperatura da base (°C) [padrão: 200]: 
Temperatura do ambiente (°C) [padrão: 25]: 
Espessura da base (m) [padrão: 0.01]: 
Comprimento da aleta (m) [padrão: 0.05]: 
Coeficiente de convecção h (W/m²K) [padrão: 15]: 
Condutividade térmica k (W/mK) [padrão: 180]: 
```

Basta pressionar **Enter** para usar os valores padrão ou digitar novos valores.

### Saída

O programa exibirá:

1. **Resultados numéricos** no terminal
2. **Dois gráficos**:
   - Perfil de temperatura em °C
   - Perfil adimensional (temperatura normalizada)
3. **Arquivo salvo**: `perfil_temperatura_aleta.png`

## 📊 Exemplo de Uso

```
==================================================
Análise de Aleta Triangular
==================================================

Temperatura da base (°C) [padrão: 200]: 150
Temperatura do ambiente (°C) [padrão: 25]: 20
Espessura da base (m) [padrão: 0.01]: 
Comprimento da aleta (m) [padrão: 0.05]: 0.08
Coeficiente de convecção h (W/m²K) [padrão: 15]: 20
Condutividade térmica k (W/mK) [padrão: 180]: 

==================================================
Resultados da Aleta Triangular
==================================================
Eficiência (η): 0.8542 (85.42%)
Efetividade (ε): 45.23
Calor dissipado por largura (q'): 4521.33 W/m
==================================================
✓ Gráfico salvo como 'perfil_temperatura_aleta.png'
```

## 🔧 Parâmetros de Entrada

| Parâmetro | Unidade | Descrição |
|-----------|--------|-----------|
| Tb | °C | Temperatura na base da aleta |
| T∞ | °C | Temperatura do fluido (ambiente) |
| t | m | Espessura da base da aleta |
| L | m | Comprimento (altura) da aleta |
| h | W/m²K | Coeficiente de transferência de calor por convecção |
| k | W/mK | Condutividade térmica do material |

## 📐 Teoria

A análise utiliza a equação de condução de calor em aletas com seção triangular:

$$\frac{d^2\theta}{dx^2} - m^2 \frac{x}{L}\theta = 0$$

Onde:
- $m = \sqrt{\frac{2h}{kt}}$ é o parâmetro característico
- $\theta = T - T_\infty$ é a temperatura adimensional

A solução é expressa em termos de funções de Bessel modificadas de primeira espécie:

$$\theta(x) = \theta_b \frac{I_0(2m(L-x))}{I_0(2mL)}$$

## 📁 Estrutura do Projeto

```
Calculo-de-transferencia-de-calor-em-aleta-triangular/
│
├── aletatriangular.py          # Script principal
├── perfil_temperatura_aleta.png # Gráfico gerado
├── README.md                    # Este arquivo
└── requirements.txt             # Dependências (opcional)
```

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'numpy'"

```bash
pip install numpy scipy matplotlib
```

### Erro: "Command not found: python"

Use `python3` em vez de `python`:

```bash
python3 aletatriangular.py
```

### Gráfico não aparece

Certifique-se de que o matplotlib está instalado corretamente e que seu sistema suporta GUI. Em ambientes sem interface gráfica, o gráfico será salvo em `perfil_temperatura_aleta.png`.

## 📄 Licença

Este projeto é fornecido como está para fins educacionais e de pesquisa.

## 👨‍💻 Autor

Sandro Eng

## 📧 Contato

Para dúvidas ou sugestões, abra uma **issue** no repositório GitHub.

---

**Desenvolvido em Python 3.x com NumPy, SciPy e Matplotlib**

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import iv # Função de Bessel modificada de primeira espécie

def obter_entrada_usuario():
    """Obtém dados de entrada do usuário manualmente"""
    print("=" * 60)
    print("ANÁLISE DE ALETA TRIANGULAR")
    print("=" * 60)
    
    try:
        Tb = float(input("\nTemperatura da base (°C) [padrão: 200]: ") or 200)
        T_inf = float(input("Temperatura do ambiente (°C) [padrão: 25]: ") or 25)
        t = float(input("Espessura da base (m) [padrão: 0.01]: ") or 0.01)
        L = float(input("Comprimento da aleta (m) [padrão: 0.05]: ") or 0.05)
        h = float(input("Coeficiente de convecção h (W/m²K) [padrão: 15]: ") or 15)
        k = float(input("Condutividade térmica k (W/mK) [padrão: 180]: ") or 180)
        
        return Tb, T_inf, t, L, h, k
    except ValueError:
        print("\nErro na entrada! Usando valores padrão.")
        return 200, 25, 0.01, 0.05, 15, 180

def calcular_aleta_triangular():
    # --- Dados de Entrada ---
    Tb, T_inf, t, L, h, k = obter_entrada_usuario()

    # --- Cálculos Intermediários ---
    theta_b = Tb - T_inf
    
    # Parâmetro característico 'm' para perfil triangular
    # m = sqrt( (2 * h) / (k * t) )
    m = np.sqrt((2 * h) / (k * t))
    
    # O argumento para a função de eficiência de aletas triangulares
    # X = 2 * m * L
    X = 2 * m * L

    # --- (a) Eficiência (eta) ---
    # Para aletas triangulares: eta = (1 / (m * L)) * (I1(2mL) / I0(2mL))
    # Onde I0 e I1 são funções de Bessel modificadas
    i0 = iv(0, X)
    i1 = iv(1, X)
    eficiencia = (1 / (m * L)) * (i1 / i0)

    # --- (b) Calor dissipado por unidade de largura (q') ---
    # Área da base por unidade de largura (Ab' = t * 1)
    # Área lateral da aleta triangular por unidade de largura: 
    # Perímetro lateral aproximado = 2 * sqrt(L^2 + (t/2)^2)
    A_aleta_linha = 2 * np.sqrt(L**2 + (t/2)**2)
    
    # Calor máximo possível (se toda a aleta estivesse a Tb)
    q_max_linha = h * A_aleta_linha * theta_b
    
    # Calor real
    q_real_linha = eficiencia * q_max_linha

    # --- (a) Efetividade (epsilon) ---
    # epsilon = q_aleta / (h * A_base * theta_b)
    # Para unidade de largura, A_base_linha = t
    efetividade = q_real_linha / (h * t * theta_b)

    # --- Resultados ---
    print(f"\n{'=' * 60}")
    print(f"Resultados da Aleta Triangular")
    print(f"{'=' * 60}")
    print(f"Eficiência (η): {eficiencia:.4f} ({eficiencia*100:.2f}%)")
    print(f"Efetividade (ε): {efetividade:.2f}")
    print(f"Calor dissipado por largura (q'): {q_real_linha:.2f} W/m")
    print(f"{'=' * 60}\n")
    
    # --- Perfil de Temperatura ---
    calcular_e_plotar_perfil_temperatura(Tb, T_inf, m, L, k, h)

def calcular_e_plotar_perfil_temperatura(Tb, T_inf, m, L, k, h):
    """Calcula e plota o perfil de temperatura ao longo da aleta (similar a FEA)"""
    
    # Discretização: criamos 100 pontos ao longo da aleta
    num_pontos = 100
    x = np.linspace(0, L, num_pontos)
    
    # A solução para temperatura em aleta triangular é dada por:
    # theta(x) / theta_b = (I0(2*m*(L-x)) / I0(2*m*L))
    # onde theta = T - T_inf
    
    X = 2 * m * L
    X_x = 2 * m * (L - x)
    
    # Temperatura adimensional
    theta_adim = iv(0, X_x) / iv(0, X)
    
    # Temperatura dimensional
    T_x = T_inf + theta_adim * (Tb - T_inf)
    
    # --- Criando o gráfico ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Gráfico 1: Perfil de Temperatura
    ax1.plot(x * 1000, T_x, 'b-', linewidth=2.5, label='Perfil de Temperatura')
    ax1.scatter([0], [Tb], color='red', s=100, zorder=5, label='Base (Tb)')
    ax1.axhline(y=T_inf, color='r', linestyle='--', linewidth=1.5, label='Ambiente (T∞)')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlabel('Posição ao longo da aleta (mm)', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Temperatura (°C)', fontsize=11, fontweight='bold')
    ax1.set_title('Perfil de Temperatura na Aleta Triangular', fontsize=12, fontweight='bold')
    ax1.legend(fontsize=10)
    
    # Gráfico 2: Temperatura Adimensional
    ax2.plot(x * 1000, theta_adim, 'g-', linewidth=2.5)
    ax2.scatter([0], [1.0], color='red', s=100, zorder=5, label='Base')
    ax2.grid(True, alpha=0.3)
    ax2.set_xlabel('Posição ao longo da aleta (mm)', fontsize=11, fontweight='bold')
    ax2.set_ylabel('θ(x)/θb = (T-T∞)/(Tb-T∞)', fontsize=11, fontweight='bold')
    ax2.set_title('Perfil Adimensional (Elementos Finitos)', fontsize=12, fontweight='bold')
    ax2.legend(fontsize=10)
    
    plt.tight_layout()
    plt.savefig('perfil_temperatura_aleta.png', dpi=300, bbox_inches='tight')
    print("✓ Gráfico salvo como 'perfil_temperatura_aleta.png'")
    plt.show()

if __name__ == "__main__":
    calcular_aleta_triangular()
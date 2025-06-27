import time

def is_coprime_with_42(n):
    for d in [2, 3, 6, 7]:
        if n % d == 0:
            return False
    return True

def crivo_becker_gpt(limit):
    coprimes_42 = [n for n in range(1, 42) if is_coprime_with_42(n)]
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]

    for base in range(2, int(limit ** 0.5) + 1):
        if sieve[base]:
            for multiple in range(base * base, limit + 1, base):
                sieve[multiple] = False

    return [num for num in range(2, limit + 1) if sieve[num] and (num % 42) in coprimes_42]

def main():
    print("Gerador de números primos baseados no crivo Becker-GPT")
    try:
        limit = int(input("Deseja números primos até qual número em média? "))
    except ValueError:
        print("Por favor, insira um número inteiro válido.")
        return

    start_time = time.time()
    primos = crivo_becker_gpt(limit)
    elapsed = time.time() - start_time

    filename = "primos_becker_gpt.txt"
    with open(filename, "w") as f:
        f.write(f"Tempo de execução: {elapsed:.4f} segundos\n")
        f.write(f"Total de primos encontrados: {len(primos)}\n\n")
        f.write(", ".join(map(str, primos)))

    print(f"\nArquivo '{filename}' gerado com sucesso.")
    print(f"Tempo de execução: {elapsed:.4f} segundos")
    print(f"Total de primos encontrados: {len(primos)}")
    print("Pressione Enter para sair.")
    input()

if __name__ == "__main__":
    main()
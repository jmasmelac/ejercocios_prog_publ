"""
PDF Password Recovery Tool
Intenta recuperar la contraseña de un PDF usando diccionario o fuerza bruta.
Úsalo solo en archivos de tu propiedad o con permiso explícito.
"""

import argparse
import itertools
import string
import sys
from pypdf import PdfReader


# ──────────────────────────────────────────────
# Método 1: Ataque por diccionario
# ──────────────────────────────────────────────
def dictionary_attack(pdf_path: str, wordlist_path: str) -> str | None:
    """Prueba cada contraseña de un archivo de diccionario."""
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            passwords = [line.strip() for line in f]
    except FileNotFoundError:
        print(f"[ERROR] No se encontró el diccionario: {wordlist_path}")
        return None

    print(f"[INFO] Probando {len(passwords):,} contraseñas del diccionario...")

    for i, password in enumerate(passwords, 1):
        if try_password(pdf_path, password):
            return password
        if i % 1000 == 0:
            print(f"  → Probadas: {i:,} / {len(passwords):,}", end="\r")

    print()
    return None


# ──────────────────────────────────────────────
# Método 2: Fuerza bruta
# ──────────────────────────────────────────────
def brute_force_attack(
    pdf_path: str,
    charset: str,
    min_len: int = 1,
    max_len: int = 4,
) -> str | None:
    """Genera y prueba todas las combinaciones posibles."""
    total = sum(len(charset) ** l for l in range(min_len, max_len + 1))
    print(f"[INFO] Fuerza bruta: {total:,} combinaciones (largo {min_len}-{max_len})")

    count = 0
    for length in range(min_len, max_len + 1):
        for combo in itertools.product(charset, repeat=length):
            password = "".join(combo)
            count += 1
            if count % 5000 == 0:
                print(f"  → Probadas: {count:,} / {total:,}  última: {password!r}", end="\r")
            if try_password(pdf_path, password):
                print()
                return password

    print()
    return None


# ──────────────────────────────────────────────
# Función auxiliar
# ──────────────────────────────────────────────
def try_password(pdf_path: str, password: str) -> bool:
    """Retorna True si la contraseña abre el PDF."""
    try:
        reader = PdfReader(pdf_path)
        if reader.is_encrypted:
            result = reader.decrypt(password)
            return result != 0  # 0 = falló, 1 = user pass, 2 = owner pass
        else:
            print("[INFO] El PDF no está protegido con contraseña.")
            sys.exit(0)
    except Exception:
        return False


# ──────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="Recupera la contraseña de un PDF (solo para uso legítimo)."
    )
    parser.add_argument("pdf", help="Ruta al archivo PDF protegido")
    parser.add_argument(
        "--mode",
        choices=["dictionary", "brute"],
        default="dictionary",
        help="Modo de ataque (default: dictionary)",
    )
    parser.add_argument(
        "--wordlist",
        default="wordlist.txt",
        help="Ruta al archivo de diccionario (modo dictionary)",
    )
    parser.add_argument(
        "--charset",
        default="digits",
        choices=["digits", "lower", "upper", "alpha", "alphanumeric", "all"],
        help="Conjunto de caracteres para fuerza bruta (default: digits)",
    )
    parser.add_argument("--min", type=int, default=1, help="Longitud mínima (brute, default: 1)")
    parser.add_argument("--max", type=int, default=4, help="Longitud máxima (brute, default: 4)")
    args = parser.parse_args()

    # Mapa de charsets
    charsets = {
        "digits":       string.digits,
        "lower":        string.ascii_lowercase,
        "upper":        string.ascii_uppercase,
        "alpha":        string.ascii_letters,
        "alphanumeric": string.ascii_letters + string.digits,
        "all":          string.printable.strip(),
    }

    print(f"\n🔐 PDF Password Recovery")
    print(f"   Archivo : {args.pdf}")
    print(f"   Modo    : {args.mode}\n")

    found = None

    if args.mode == "dictionary":
        found = dictionary_attack(args.pdf, args.wordlist)
    else:
        charset = charsets[args.charset]
        found = brute_force_attack(args.pdf, charset, args.min, args.max)

    if found:
        print(f"\n✅ ¡Contraseña encontrada!: {found!r}")
    else:
        print("\n❌ No se encontró la contraseña con los parámetros dados.")
        print("   Sugerencias:")
        print("   - Usa un diccionario más grande (ej: rockyou.txt)")
        print("   - Aumenta el rango de longitud con --min y --max")
        print("   - Prueba un charset diferente con --charset")


if __name__ == "__main__":
    main()
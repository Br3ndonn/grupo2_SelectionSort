# 🔍 Comparação: C vs Java vs Python - Formatação CSV

## 📊 Tabela Comparativa

| Aspecto | C | Java | Python |
|---------|---|------|--------|
| **Problema de Locale?** | ❌ Não | ✅ **SIM** | ❌ Não |
| **Separador Decimal** | Ponto (.) | Depende do Locale | Ponto (.) |
| **Solução Necessária** | - | `Locale.US` | - |
| **Automaticamente Correto** | ✅ Sim | ❌ Não | ✅ Sim |

## 🔧 Implementações

### 1️⃣ C - Correto por Padrão
```c
fprintf(resultado, "%d,%.6f,%.6f\n", n, media, desvio);
```
**✅ Funciona corretamente sem configuração adicional**

- `printf` e `fprintf` usam ponto decimal por padrão
- Não é afetado por configurações regionais
- Segue o padrão da linguagem C (ANSI C)

---

### 2️⃣ Java - Requer Correção ⚠️

#### ❌ ERRADO (código original):
```java
writer.printf("%d,%.6f,%.6f%n", n, media, desvio);
```
**Problema**: Usa `Locale` padrão do sistema (pt_BR = vírgula)

#### ✅ CORRETO (após correção):
```java
import java.util.Locale;

writer.printf(Locale.US, "%d,%.6f,%.6f%n", n, media, desvio);
```
**Solução**: Especifica `Locale.US` explicitamente

**Por quê?**
- Java é multi-idioma por design
- `printf()` sem Locale usa `Locale.getDefault()`
- No Brasil: `Locale.getDefault()` = `pt_BR`
- `pt_BR` usa vírgula como separador decimal

---

### 3️⃣ Python - Correto por Design
```python
import csv

writer = csv.writer(f)
writer.writerow([n, f"{media:.6f}", f"{desvio:.6f}"])
```
**✅ Módulo `csv` usa ponto decimal automaticamente**

- O módulo `csv` segue RFC 4180
- f-strings usam ponto independente do locale
- Comportamento consistente e previsível

---

## 🐛 Exemplo do Problema (Java sem correção)

### Sistema configurado em pt_BR:

#### Código:
```java
double valor = 123.456789;
System.out.printf("%.6f%n", valor);  // Console
writer.printf("%.6f%n", valor);       // Arquivo
```

#### Saída:
```
123,456789  ❌ (vírgula no arquivo CSV)
```

#### No CSV:
```csv
n,tempo_ms,desvio
10000,45,234567,2,567890  ❌ 5 colunas!
```

---

## ✅ Após Correção (Java)

#### Código:
```java
double valor = 123.456789;
writer.printf(Locale.US, "%.6f%n", valor);
```

#### Saída:
```
123.456789  ✅ (ponto no arquivo CSV)
```

#### No CSV:
```csv
n,tempo_ms,desvio
10000,45.234567,2.567890  ✅ 3 colunas!
```

---

## 🎯 Por que cada linguagem é diferente?

### C - Simplicidade
- Linguagem de baixo nível
- Sem suporte nativo a internacionalização
- Comportamento consistente e previsível
- **Vantagem**: Funciona sempre
- **Desvantagem**: Difícil adaptar para outros idiomas

### Java - Internacionalização
- Design voltado para aplicações globais
- Suporte robusto a múltiplos idiomas
- Locale configurável por usuário/sistema
- **Vantagem**: Flexível para i18n
- **Desvantagem**: Requer atenção com CSV

### Python - Pragmatismo
- Módulos seguem padrões internacionais
- CSV module implementa RFC 4180
- f-strings não são afetadas por locale
- **Vantagem**: "Batteries included" correto
- **Desvantagem**: Formato local requer locale module

---

## 📝 Melhores Práticas

### ✅ Para CSV - Use SEMPRE ponto decimal:

```c
// C - já correto
fprintf(f, "%.6f", valor);
```

```java
// Java - especificar Locale
writer.printf(Locale.US, "%.6f", valor);
// ou
String.format(Locale.US, "%.6f", valor);
```

```python
# Python - módulo csv
writer = csv.writer(f)
writer.writerow([f"{valor:.6f}"])
# ou
import locale
locale.setlocale(locale.LC_ALL, 'C')
```

---

## 🧪 Como Testar

### Teste em cada linguagem:

#### C:
```bash
cd codigo/c
./main.exe 10000
type ..\..\resultados\estatisticas\resultados_C.csv
```

#### Java:
```bash
cd codigo/java
java Main 10000
type ..\..\resultados\estatisticas\resultados_Java.csv
```

#### Python:
```bash
cd codigo/python
python main.py 10000
type ..\..\resultados\estatisticas\resultados_Python.csv
```

### ✅ Resultado Esperado (todos iguais):
```csv
n,tempo_ms,desvio
10000,45.234567,2.567890
```

---

## 📊 Resultados dos Testes

| Implementação | Antes | Depois |
|---------------|-------|--------|
| C | ✅ Correto | ✅ Correto |
| Java | ❌ Vírgula | ✅ Ponto |
| Python | ✅ Correto | ✅ Correto |

---

## 🎓 Lições Aprendidas

1. **CSV requer ponto decimal**: Padrão RFC 4180
2. **Java não é automático**: Requer `Locale.US`
3. **C é simples**: Sem surpresas
4. **Python é pragmático**: Módulos seguem padrões
5. **Sempre testar**: Especialmente em sistemas pt_BR

---

## 📚 Referências

- [RFC 4180 - CSV Specification](https://tools.ietf.org/html/rfc4180)
- [Java Locale](https://docs.oracle.com/javase/tutorial/i18n/locale/)
- [Python CSV Module](https://docs.python.org/3/library/csv.html)
- [C printf](https://www.cplusplus.com/reference/cstdio/printf/)

---

**Resumo**: Java foi o único que precisou de correção. C e Python já estavam corretos! ✅

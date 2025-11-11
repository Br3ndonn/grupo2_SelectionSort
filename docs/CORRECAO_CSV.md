# Correção do Formato de Números Decimais no CSV - Java

## 🐛 Problema Identificado

O código Java estava usando o `Locale` padrão do sistema para formatar números decimais. Em sistemas configurados para português do Brasil, isso resultava em números sendo salvos com **vírgula** como separador decimal (ex: `123,456`) ao invés de **ponto** (ex: `123.456`), o que causava problemas ao ler o arquivo CSV.

### Exemplo do problema:
```csv
n,tempo_ms,desvio
10000,45,234,2,567    ❌ ERRADO (vírgulas extras confundem o parser CSV)
```

### Como deveria ser:
```csv
n,tempo_ms,desvio
10000,45.234,2.567    ✅ CORRETO (ponto como separador decimal)
```

## ✅ Solução Implementada

### Código Antes:
```java
writer.printf("%d,%.6f,%.6f%n", n, media, desvio);
```

### Código Depois:
```java
// Importar Locale
import java.util.Locale;

// Na hora de escrever no arquivo CSV
writer.printf(Locale.US, "%d,%.6f,%.6f%n", n, media, desvio);
```

## 🔍 Explicação Técnica

### O que é Locale?
`Locale` define as convenções de formatação regionais, incluindo:
- Separador decimal (ponto ou vírgula)
- Separador de milhares
- Formato de data/hora
- Símbolo de moeda

### Por que `Locale.US`?
- **Locale.US** usa o padrão internacional para CSV
- Separador decimal: **ponto** (.)
- Compatível com ferramentas de análise de dados (Excel, Python, R, etc.)
- Padrão recomendado pela RFC 4180 (especificação CSV)

### Diferença entre Locales:

| Locale | Número | Formato |
|--------|--------|---------|
| pt_BR | 1234.56 | `"1.234,56"` |
| en_US | 1234.56 | `"1,234.56"` ou `"1234.56"` |
| Locale.US | 1234.56 | `"1234.56"` ✅ (ideal para CSV) |

## 📝 Mudanças Realizadas

### 1. Import adicionado:
```java
import java.util.Locale;
```

### 2. Linha 91 - Escrita no arquivo CSV:
```java
// Antes:
writer.printf("%d,%.6f,%.6f%n", n, media, desvio);

// Depois:
writer.printf(Locale.US, "%d,%.6f,%.6f%n", n, media, desvio);
```

### 3. Comentários explicativos:
```java
// Usa formatação com ponto decimal (Locale.US) para garantir compatibilidade CSV
writer.printf(Locale.US, "%d,%.6f,%.6f%n", n, media, desvio);

// Exibe no console usando a localização do sistema para melhor legibilidade
System.out.printf("  Media: %.3f ms, Desvio: %.3f ms%n", media, desvio);
```

## 🎯 Benefícios da Solução

1. **Compatibilidade Universal**: CSV funciona em qualquer ferramenta
2. **Sem Ambiguidade**: Ponto sempre como decimal, vírgula sempre como separador
3. **Padrão Internacional**: Segue RFC 4180
4. **Legibilidade Mantida**: Console ainda usa o formato local do usuário
5. **Simples e Eficiente**: Uma linha de código resolve o problema

## 🧪 Como Testar

### 1. Compilar:
```bash
javac Main.java CarregaCSV.java SelectionSort.java
# ou
compilar.bat
```

### 2. Executar:
```bash
java Main
```

### 3. Verificar resultado:
```bash
cat ../../resultados/estatisticas/resultados_Java.csv
```

**Saída esperada:**
```csv
n,tempo_ms,desvio
10000,45.234567,2.567890
20000,180.456789,5.123456
...
```

## 📊 Comparação: Antes vs Depois

### Antes (com problema):
```csv
n,tempo_ms,desvio
10000,45,234567,2,567890
```
- ❌ 5 colunas ao invés de 3
- ❌ Impossível fazer parse correto
- ❌ Gera erro em análises

### Depois (corrigido):
```csv
n,tempo_ms,desvio
10000,45.234567,2.567890
```
- ✅ 3 colunas corretas
- ✅ Parse funciona perfeitamente
- ✅ Compatível com todas as ferramentas

## 🔧 Alternativas Consideradas

### Alternativa 1: String.format com Locale
```java
String linha = String.format(Locale.US, "%d,%.6f,%.6f", n, media, desvio);
writer.println(linha);
```
- Funciona, mas mais verboso

### Alternativa 2: DecimalFormat
```java
DecimalFormat df = new DecimalFormat("0.000000", DecimalFormatSymbols.getInstance(Locale.US));
writer.printf("%d,%s,%s%n", n, df.format(media), df.format(desvio));
```
- Mais complexo, sem ganho real

### ✅ Solução Escolhida: printf com Locale.US
- Mais simples e direta
- Melhor performance
- Código mais limpo e legível

## 📚 Referências

- [RFC 4180 - CSV Format](https://tools.ietf.org/html/rfc4180)
- [Java Locale Documentation](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Locale.html)
- [Java PrintWriter Documentation](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/PrintWriter.html)

---

**Problema resolvido! O CSV agora usa ponto como separador decimal em todas as situações. ✅**

import java.io.*;
import java.util.*;

public class Main {

    private static double executarExperimento(String caminhoCSV) {
        try {
            int[] arr = CarregaCSV.carregar(caminhoCSV);

            long tInicio = System.nanoTime();
            SelectionSort.sort(arr);
            long tFim = System.nanoTime();

            return (tFim - tInicio) / 1_000_000.0;
        } catch (IOException e) {
            System.err.println("Erro ao carregar arquivo: " + caminhoCSV);
            return -1.0;
        }
    }

    private static double calcularMedia(double[] valores) {
        double soma = 0.0;
        for (double v : valores) soma += v;
        return soma / valores.length;
    }

    private static double calcularDesvio(double[] valores, double media) {
        if (valores.length <= 1) return 0.0;
        double soma = 0.0;
        for (double v : valores) soma += Math.pow(v - media, 2);
        return Math.sqrt(soma / (valores.length - 1));
    }

    public static void main(String[] args) {
        System.out.println("EXPERIMENTOS - SELECTION SORT (JAVA)");

        // 🔹 Caminho da pasta "dados" relativo ao projeto
        File pastaDados = new File("dados");
        if (!pastaDados.exists() || !pastaDados.isDirectory()) {
            System.err.println("Pasta de dados não encontrada: " + pastaDados.getAbsolutePath());
            System.exit(1);
        }

        // 🔹 Lista todas as subpastas (n010000, n020000, etc.)
        File[] pastasTamanho = pastaDados.listFiles(File::isDirectory);
        if (pastasTamanho == null || pastasTamanho.length == 0) {
            System.err.println("Nenhuma subpasta encontrada dentro de " + pastaDados.getAbsolutePath());
            System.exit(1);
        }

        // 🔹 Ordena as pastas pelo nome (para garantir ordem crescente)
        Arrays.sort(pastasTamanho, Comparator.comparing(File::getName));

        File pastaResultados = new File("resultados/estatisticas");
        pastaResultados.mkdirs();

        try (PrintWriter writer = new PrintWriter(new FileWriter(
                new File(pastaResultados, "resultados_Java.csv")))) {
            writer.println("n,tempo_ms,desvio");

            for (File pasta : pastasTamanho) {
                String nomePasta = pasta.getName(); // ex: "n010000"
                int n = Integer.parseInt(nomePasta.substring(1)); // pega 10000, 20000, etc.
                System.out.println("\nProcessando " + nomePasta + " (n=" + n + ")...");

                File[] arquivosCSV = pasta.listFiles((dir, nome) -> nome.endsWith(".csv"));
                if (arquivosCSV == null || arquivosCSV.length == 0) {
                    System.err.println("Nenhum CSV encontrado em " + pasta.getPath());
                    continue;
                }

                Arrays.sort(arquivosCSV, Comparator.comparing(File::getName));

                double[] tempos = new double[arquivosCSV.length];
                int validos = 0;

                for (File csv : arquivosCSV) {
                    double tempo = executarExperimento(csv.getPath());
                    if (tempo >= 0) tempos[validos++] = tempo;

                    if (validos % 10 == 0)
                        System.out.println("  Execuções processadas: " + validos + "/" + arquivosCSV.length);
                }

                if (validos > 0) {
                    double[] temposValidos = Arrays.copyOf(tempos, validos);
                    double media = calcularMedia(temposValidos);
                    double desvio = calcularDesvio(temposValidos, media);

                    writer.printf("%d,%.6f,%.6f%n", n, media, desvio);
                    System.out.printf("  Média: %.3f ms | Desvio: %.3f ms%n", media, desvio);
                }
            }

        } catch (IOException e) {
            System.err.println("Erro ao criar arquivo de resultados: " + e.getMessage());
            System.exit(1);
        }

        System.out.println("\nResultados em: resultados/estatisticas/resultados_Java.csv");
    }
}

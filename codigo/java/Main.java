import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Locale;

public class Main {
    
    private static double executarExperimento(String caminhoCSV) {
        try {
            int[] arr = CarregaCSV.carregar(caminhoCSV);
            
            long tInicio = System.nanoTime();
            SelectionSort.sort(arr);
            long tFim = System.nanoTime();
            
            return (tFim - tInicio) / 1_000_000.0; // Retorna em milissegundos
        } catch (IOException e) {
            return -1.0;
        }
    }
    
    private static double calcularMedia(double[] valores) {
        double soma = 0.0;
        for (double v : valores) {
            soma += v;
        }
        return soma / valores.length;
    }
    
    private static double calcularDesvio(double[] valores, double media) {
        if (valores.length <= 1) return 0.0;
        
        double soma = 0.0;
        for (double v : valores) {
            double diff = v - media;
            soma += diff * diff;
        }
        return Math.sqrt(soma / (valores.length - 1));
    }
    
    public static void main(String[] args) {
        int[] tamanhos = {10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000};
        int numExecucoes = 50;
        
        if (args.length > 0) {
            tamanhos = new int[args.length];
            for (int i = 0; i < args.length; i++) {
                tamanhos[i] = Integer.parseInt(args[i]);
            }
        }
        
        System.out.println("EXPERIMENTOS - SELECTION SORT (JAVA)");
        
        new File("../../resultados/estatisticas").mkdirs();
        
        try (PrintWriter writer = new PrintWriter(new FileWriter("../../resultados/estatisticas/resultados_Java.csv"))) {
            writer.println("n,tempo_ms,desvio");
            
            for (int n : tamanhos) {
                System.out.println("\nProcessando n=" + n + "...");
                
                double[] tempos = new double[numExecucoes];
                int validos = 0;
                
                for (int exec = 1; exec <= numExecucoes; exec++) {
                    String caminho = String.format("../../dados/n%06d/run_%03d.csv", n, exec);
                    
                    double tempo = executarExperimento(caminho);
                    if (tempo >= 0) {
                        tempos[validos++] = tempo;
                    }
                    
                    if (exec % 10 == 0) {
                        System.out.println("  " + exec + "/" + numExecucoes);
                    }
                }
                
                if (validos > 0) {
                    double[] temposValidos = new double[validos];
                    System.arraycopy(tempos, 0, temposValidos, 0, validos);
                    
                    double media = calcularMedia(temposValidos);
                    double desvio = calcularDesvio(temposValidos, media);
                    
                    // Usa formatação com ponto decimal (Locale.US) para garantir compatibilidade CSV
                    writer.printf(Locale.US, "%d,%.6f,%.6f%n", n, media, desvio);
                    
                    // Exibe no console usando a localização do sistema para melhor legibilidade
                    System.out.printf("  Media: %.3f ms, Desvio: %.3f ms%n", media, desvio);
                }
            }
            
        } catch (IOException e) {
            System.err.println("Erro ao criar arquivo de resultados: " + e.getMessage());
            System.exit(1);
        }
        
        System.out.println("\nResultados em: resultados/estatisticas/resultados_Java.csv");
    }
}

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.*;

public class CarregaCSV {
    
    public static int[] carregar(String caminho) throws IOException {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(
                new FileInputStream(caminho), StandardCharsets.UTF_8))) {
            
            String linha = br.readLine();
            if (linha == null || linha.trim().isEmpty()) {
                return new int[0];
            }

            // 🔹 Remove possíveis \r (caracteres de quebra de linha do Windows)
            linha = linha.trim().replace("\r", "");

            // 🔹 Garante que apenas números válidos sejam processados
            String[] tokens = linha.split(",");
            List<Integer> numeros = new ArrayList<>();

            for (String token : tokens) {
                token = token.trim();
                if (!token.isEmpty()) {
                    try {
                        numeros.add(Integer.parseInt(token));
                    } catch (NumberFormatException e) {
                        System.err.println("Valor inválido ignorado: " + token + " em " + caminho);
                    }
                }
            }

            // 🔹 Converte lista para array primitivo
            int[] arr = new int[numeros.size()];
            for (int i = 0; i < numeros.size(); i++) {
                arr[i] = numeros.get(i);
            }

            return arr;
        }
    }
}

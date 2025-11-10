import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class CarregaCSV {
    
    public static int[] carregar(String caminho) throws IOException {
        try (BufferedReader br = new BufferedReader(new FileReader(caminho))) {
            String linha = br.readLine();
            if (linha == null || linha.trim().isEmpty()) {
                return new int[0];
            }
            
            String[] tokens = linha.split(",");
            int[] arr = new int[tokens.length];
            
            for (int i = 0; i < tokens.length; i++) {
                arr[i] = Integer.parseInt(tokens[i].trim());
            }
            
            return arr;
        }
    }
}

import java.io.IOException;
import java.io.PrintStream;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

public class Client {
 public static void main(String[] args) 
                 throws UnknownHostException, IOException {
     Socket cliente = new Socket("", 7000);
     System.out.println("O cliente se conectou ao servidor!");

     Scanner teclado = new Scanner(System.in);
     PrintStream saida = new PrintStream(cliente.getOutputStream());

     while (teclado.hasNextLine()) {
         saida.println(teclado.nextLine());
     }

     saida.close();
     teclado.close();
     cliente.close();
 }
}

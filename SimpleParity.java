import java.nio.charset.StandardCharsets;
import java.util.BitSet;

public class SimpleParity {

    public static void main(String[] args) {
        String message = "Secret message!!";
        BitSet bitSet = BitSet.valueOf(message.getBytes(StandardCharsets.UTF_8));
        parity(bitSet, message.length() * 8);
    }

    public static void parity(BitSet bitSet, int bitLength) {
        System.out.println("Original:\t\t\t" + bitSet);
        int count = bitSet.cardinality();
        System.out.println("Counted " + count + " 1's in bitarray");
        boolean pbit = (count % 2) != 0;
        System.out.println("Parity bit is " + (pbit ? 1 : 0));
        bitSet.set(bitLength, pbit);
        System.out.println("Parity bitarray: \t" + bitSet);
    }
}

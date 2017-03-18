import java.util.*;

/**
 * Auto-generated code below aims at helping you parse the standard input
 * according to the problem statement.
 *
 */
class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt(); // Number of elements which make up the association table.
        int Q = in.nextInt(); // Number Q of file names to be analyzed.
        Map<String, String> mimes = new HashMap<>();
        for (int i = 0; i < N; i++) {
            String EXT = in.next().toLowerCase(); // file extension
            System.err.println("Map ext: " + EXT);
            String MT = in.next(); // MIME type.
            System.err.println("Map mime: " + MT);
            mimes.put(EXT, MT);
        }
        List<String> files = new ArrayList<>();
        in.nextLine();
        for (int i = 0; i < Q; i++) {
            String FNAME = in.nextLine().toLowerCase(); // One file name per line.
            System.err.println("File name: " + FNAME);
            int dot = FNAME.lastIndexOf(".");
            String ext = "bluff";
            if (!(dot < 0)) {
                ext = FNAME.substring(dot + 1, FNAME.length());
            }
            System.err.println("File ext: " + ext);
            String mime = mimes.getOrDefault(ext, "UNKNOWN");
            System.out.println(mime);

        }

        // Write an action using System.out.println()
        // To debug: System.err.println("Debug messages...");
        // For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
    }
}
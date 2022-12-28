package tw.com.jchang.geniiecgbt;

/**
 * Created by User on 12/11/2017.
 */

public class decompNDK {
    static {
        System.loadLibrary("myDecompJNI");
    }
    public native  int decpEcgFile(String path);
}

import java.util.*;

public class Bubblesort {
	public static void bubbleSort(int[] arr) {
		int n = arr.length;
		if (n < 2) return;

		for (int end = n - 1; end > 0; end--) {
			boolean swapped = false;
			for (int i = 0; i < end; i++) {
				if (arr[i] > arr[i + 1]) {
					int tmp = arr[i];
					arr[i] = arr[i + 1];
					arr[i + 1] = tmp;
					swapped = true;
				}
			}
			if (!swapped) break; // already sorted
		}
	}

	private static String arrayToString(int[] a) {
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < a.length; i++) {
			if (i > 0) sb.append(' ');
			sb.append(a[i]);
		}
		return sb.toString();
	}

	public static void main(String[] args) {

		int[] arr;

		if (args != null && args.length > 0) {
			arr = new int[args.length];
			for (int i = 0; i < args.length; i++) arr[i] = Integer.parseInt(args[i]);
		} else {
			Scanner sc = new Scanner(System.in);
			System.out.println("Enter integers separated by space:");
			String line = sc.hasNextLine() ? sc.nextLine().trim() : "";
			if (line.isEmpty()) {
				arr = new int[] {5, 2, 9, 1, 5, 6}; 
			} else {
				String[] parts = line.split("\\s+");
				arr = new int[parts.length];
				for (int i = 0; i < parts.length; i++) arr[i] = Integer.parseInt(parts[i]);
			}
			sc.close();
		}

		bubbleSort(arr);
		System.out.println("Sorted: " + arrayToString(arr));
	}
}


/**
 * Binary Search Tree Implementation in Java
 * 
 * This class provides a complete implementation of a Binary Search Tree (BST)
 * with common operations including insertion, deletion, searching, and traversals.
 * 
 * Features:
 * - Insert nodes
 * - Delete nodes (handles all cases: leaf, one child, two children)
 * - Search for values
 * - Find minimum and maximum values
 * - Three types of traversals (Inorder, Preorder, Postorder)
 * - Calculate tree height
 * - Count total nodes
 * - Check if tree is balanced
 * 
 * @author Hacktoberfest 2025 Contributor
 * @version 1.0
 * @since October 2025
 */

public class BinarySearchTree {
    
    /**
     * Inner class representing a node in the BST
     */
    private class Node {
        int data;
        Node left;
        Node right;
        
        /**
         * Constructor to create a new node
         * @param data The value to store in the node
         */
        public Node(int data) {
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }
    
    private Node root;
    
    /**
     * Constructor to create an empty BST
     */
    public BinarySearchTree() {
        this.root = null;
    }
    
    // ==================== Insertion Operations ====================
    
    /**
     * Public method to insert a value into the BST
     * @param data The value to insert
     */
    public void insert(int data) {
        root = insertRec(root, data);
        System.out.println("Inserted: " + data);
    }
    
    /**
     * Recursive helper method to insert a value
     * @param root The root of the current subtree
     * @param data The value to insert
     * @return The root of the modified subtree
     */
    private Node insertRec(Node root, int data) {
        // Base case: if tree is empty, create new node
        if (root == null) {
            root = new Node(data);
            return root;
        }
        
        // Recursively insert in left or right subtree
        if (data < root.data) {
            root.left = insertRec(root.left, data);
        } else if (data > root.data) {
            root.right = insertRec(root.right, data);
        }
        
        // Return unchanged root pointer
        return root;
    }
    
    // ==================== Deletion Operations ====================
    
    /**
     * Public method to delete a value from the BST
     * @param data The value to delete
     */
    public void delete(int data) {
        root = deleteRec(root, data);
        System.out.println("Deleted: " + data);
    }
    
    /**
     * Recursive helper method to delete a value
     * @param root The root of the current subtree
     * @param data The value to delete
     * @return The root of the modified subtree
     */
    private Node deleteRec(Node root, int data) {
        // Base case: if tree is empty
        if (root == null) {
            return root;
        }
        
        // Recursively find the node to delete
        if (data < root.data) {
            root.left = deleteRec(root.left, data);
        } else if (data > root.data) {
            root.right = deleteRec(root.right, data);
        } else {
            // Node found: handle three cases
            
            // Case 1: Node with only one child or no child
            if (root.left == null) {
                return root.right;
            } else if (root.right == null) {
                return root.left;
            }
            
            // Case 2: Node with two children
            // Get inorder successor (smallest in right subtree)
            root.data = minValue(root.right);
            
            // Delete the inorder successor
            root.right = deleteRec(root.right, root.data);
        }
        
        return root;
    }
    
    /**
     * Find the minimum value in a subtree
     * @param root The root of the subtree
     * @return The minimum value
     */
    private int minValue(Node root) {
        int minValue = root.data;
        while (root.left != null) {
            minValue = root.left.data;
            root = root.left;
        }
        return minValue;
    }
    
    // ==================== Search Operations ====================
    
    /**
     * Public method to search for a value in the BST
     * @param data The value to search for
     * @return true if found, false otherwise
     */
    public boolean search(int data) {
        return searchRec(root, data);
    }
    
    /**
     * Recursive helper method to search for a value
     * @param root The root of the current subtree
     * @param data The value to search for
     * @return true if found, false otherwise
     */
    private boolean searchRec(Node root, int data) {
        // Base cases: root is null or data is at root
        if (root == null) {
            return false;
        }
        if (root.data == data) {
            return true;
        }
        
        // Recursively search in left or right subtree
        if (data < root.data) {
            return searchRec(root.left, data);
        }
        return searchRec(root.right, data);
    }
    
    // ==================== Traversal Operations ====================
    
    /**
     * Inorder traversal (Left-Root-Right)
     * Prints elements in sorted order
     */
    public void inorderTraversal() {
        System.out.print("Inorder Traversal: ");
        inorderRec(root);
        System.out.println();
    }
    
    private void inorderRec(Node root) {
        if (root != null) {
            inorderRec(root.left);
            System.out.print(root.data + " ");
            inorderRec(root.right);
        }
    }
    
    /**
     * Preorder traversal (Root-Left-Right)
     */
    public void preorderTraversal() {
        System.out.print("Preorder Traversal: ");
        preorderRec(root);
        System.out.println();
    }
    
    private void preorderRec(Node root) {
        if (root != null) {
            System.out.print(root.data + " ");
            preorderRec(root.left);
            preorderRec(root.right);
        }
    }
    
    /**
     * Postorder traversal (Left-Right-Root)
     */
    public void postorderTraversal() {
        System.out.print("Postorder Traversal: ");
        postorderRec(root);
        System.out.println();
    }
    
    private void postorderRec(Node root) {
        if (root != null) {
            postorderRec(root.left);
            postorderRec(root.right);
            System.out.print(root.data + " ");
        }
    }
    
    // ==================== Utility Methods ====================
    
    /**
     * Find the minimum value in the entire tree
     * @return The minimum value
     */
    public int findMin() {
        if (root == null) {
            throw new IllegalStateException("Tree is empty");
        }
        Node current = root;
        while (current.left != null) {
            current = current.left;
        }
        return current.data;
    }
    
    /**
     * Find the maximum value in the entire tree
     * @return The maximum value
     */
    public int findMax() {
        if (root == null) {
            throw new IllegalStateException("Tree is empty");
        }
        Node current = root;
        while (current.right != null) {
            current = current.right;
        }
        return current.data;
    }
    
    /**
     * Calculate the height of the tree
     * @return The height of the tree
     */
    public int height() {
        return heightRec(root);
    }
    
    private int heightRec(Node root) {
        if (root == null) {
            return 0;
        }
        int leftHeight = heightRec(root.left);
        int rightHeight = heightRec(root.right);
        return Math.max(leftHeight, rightHeight) + 1;
    }
    
    /**
     * Count the total number of nodes in the tree
     * @return The number of nodes
     */
    public int countNodes() {
        return countNodesRec(root);
    }
    
    private int countNodesRec(Node root) {
        if (root == null) {
            return 0;
        }
        return 1 + countNodesRec(root.left) + countNodesRec(root.right);
    }
    
    /**
     * Check if the tree is balanced
     * A tree is balanced if the heights of two subtrees differ by at most 1
     * @return true if balanced, false otherwise
     */
    public boolean isBalanced() {
        return isBalancedRec(root) != -1;
    }
    
    private int isBalancedRec(Node root) {
        if (root == null) {
            return 0;
        }
        
        int leftHeight = isBalancedRec(root.left);
        if (leftHeight == -1) return -1;
        
        int rightHeight = isBalancedRec(root.right);
        if (rightHeight == -1) return -1;
        
        if (Math.abs(leftHeight - rightHeight) > 1) {
            return -1;
        }
        
        return Math.max(leftHeight, rightHeight) + 1;
    }
    
    /**
     * Check if the tree is empty
     * @return true if empty, false otherwise
     */
    public boolean isEmpty() {
        return root == null;
    }
    
    // ==================== Main Method for Testing ====================
    
    /**
     * Main method to demonstrate BST operations
     */
    public static void main(String[] args) {
        BinarySearchTree bst = new BinarySearchTree();
        
        System.out.println("=".repeat(50));
        System.out.println("Binary Search Tree Implementation Demo");
        System.out.println("=".repeat(50));
        
        // Insert elements
        System.out.println("\n1. Inserting elements: 50, 30, 70, 20, 40, 60, 80");
        int[] elements = {50, 30, 70, 20, 40, 60, 80};
        for (int element : elements) {
            bst.insert(element);
        }
        
        // Traversals
        System.out.println("\n2. Tree Traversals:");
        bst.inorderTraversal();
        bst.preorderTraversal();
        bst.postorderTraversal();
        
        // Search operations
        System.out.println("\n3. Search Operations:");
        System.out.println("Searching for 40: " + (bst.search(40) ? "Found" : "Not Found"));
        System.out.println("Searching for 90: " + (bst.search(90) ? "Found" : "Not Found"));
        
        // Min and Max
        System.out.println("\n4. Min and Max:");
        System.out.println("Minimum value: " + bst.findMin());
        System.out.println("Maximum value: " + bst.findMax());
        
        // Tree properties
        System.out.println("\n5. Tree Properties:");
        System.out.println("Height: " + bst.height());
        System.out.println("Total nodes: " + bst.countNodes());
        System.out.println("Is balanced: " + (bst.isBalanced() ? "Yes" : "No"));
        
        // Delete operations
        System.out.println("\n6. Delete Operations:");
        bst.delete(20); // Delete leaf node
        bst.delete(30); // Delete node with two children
        bst.delete(50); // Delete root
        
        System.out.println("\nAfter deletions:");
        bst.inorderTraversal();
        System.out.println("Total nodes: " + bst.countNodes());
        
        System.out.println("\n" + "=".repeat(50));
        System.out.println("Demo completed!");
        System.out.println("=".repeat(50));
    }
}

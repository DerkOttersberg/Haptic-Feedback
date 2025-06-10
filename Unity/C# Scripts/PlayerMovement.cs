using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    public float walkSpeed = 5f;
    public float runSpeed = 10f;
    public float jumpForce = 5f;  // New variable for jump force
    private float currentSpeed;

    public Transform cameraTransform;
    private Rigidbody rb;  // Reference to the Rigidbody
    private bool isGrounded;  // Check if the player is grounded

    public LayerMask groundMask;  // LayerMask to define what is ground
    public float groundCheckDistance = 0.2f;  // Distance to check for the ground

    void Start()
    {
        rb = GetComponent<Rigidbody>();  // Get the Rigidbody component
    }

    void Update()
    {
        MovePlayer();

        // Jumping logic
        if (Input.GetKeyDown(KeyCode.Space) && isGrounded)
        {
            Jump();
        }

        // Ground check to ensure player can only jump when grounded
        CheckIfGrounded();
    }

    void MovePlayer()
    {
        // Handle running
        if (Input.GetKey(KeyCode.LeftShift) || Input.GetKey(KeyCode.RightShift))
        {
            currentSpeed = runSpeed;
        }
        else
        {
            currentSpeed = walkSpeed;
        }

        // Movement input
        float moveHorizontal = Input.GetAxis("Horizontal");
        float moveVertical = Input.GetAxis("Vertical");

        Vector3 forward = cameraTransform.forward;
        Vector3 right = cameraTransform.right;

        forward.y = 0f;
        right.y = 0f;

        forward.Normalize();
        right.Normalize();

        Vector3 movement = forward * moveVertical + right * moveHorizontal;
        transform.Translate(movement * currentSpeed * Time.deltaTime, Space.World);
    }

    void Jump()
    {
        rb.AddForce(Vector3.up * jumpForce, ForceMode.Impulse);  // Apply upward force for jumping
    }

    void CheckIfGrounded()
    {
        // Perform a raycast downwards to check if the player is standing on the ground
        isGrounded = Physics.Raycast(transform.position, Vector3.down, groundCheckDistance, groundMask);
    }
}

using UnityEngine;

public class PickupThrow : MonoBehaviour
{
    public Transform player;
    public Transform playerCam;
    public Transform leftHandGrabPoint;
    public Transform rightHandGrabPoint;
    public float throwForce = 10f;
    public float holdDistance = 2f;  // This can be fine-tuned if needed
    public float moveSpeed = 2f;  // Speed of object movement while holding

    private bool isCarried = false;
    private Rigidbody rb;

    void Start()
    {
        rb = GetComponent<Rigidbody>();  // Get the Rigidbody component
    }

    void Update()
    {
        float dist = Vector3.Distance(gameObject.transform.position, player.position);

        // Pickup the object if within range and not already carried
        if (dist <= holdDistance && Input.GetKeyDown(KeyCode.E) && !isCarried)
        {
            PickUpObject();
        }
        // Drop the object if being carried
        else if (isCarried && Input.GetKeyDown(KeyCode.E))
        {
            DropObject();
        }
        // Throw the object if being carried and mouse button is released
        else if (isCarried && Input.GetMouseButtonUp(0))
        {
            ThrowObject();
        }

        // Move the object while it is being carried
        if (isCarried)
        {
            CarryObject();
        }
    }

    void PickUpObject()
    {
        rb.isKinematic = true;  // Disable physics while holding the object
        isCarried = true;

        // Move the object to the midpoint between the hands
        Vector3 holdPosition = (leftHandGrabPoint.position + rightHandGrabPoint.position) / 2;
        transform.position = holdPosition;

        // Optionally, parent the object to the player so it moves with the hands
        transform.parent = player;  // This ensures it stays with the player
    }

    void DropObject()
    {
        rb.isKinematic = false;  // Re-enable physics when dropping the object
        isCarried = false;
        transform.parent = null;  // Unparent the object from the player
    }

    void ThrowObject()
    {
        rb.isKinematic = false;
        transform.parent = null;  // Unparent the object from the player
        rb.AddForce(playerCam.forward * throwForce, ForceMode.Impulse);  // Apply throw force
        isCarried = false;
    }

    void CarryObject()
    {
        // Keep the object at the midpoint between the two hands (left and right grab points)
        Vector3 holdPosition = (leftHandGrabPoint.position + rightHandGrabPoint.position) / 2;
        transform.position = holdPosition;  // Lock the object's position to between the hands
    }
}

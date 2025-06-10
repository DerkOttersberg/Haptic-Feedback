using UnityEngine;

public class PlayerBodyColorChange : MonoBehaviour
{
    public Renderer playerRenderer; // Assign the player's body mesh renderer in the inspector
    public Renderer[] armRenderers; // Assign the arm renderers in the inspector

    private void OnTriggerEnter(Collider other)
    {
        // Check if the object we collided with has a tag that corresponds to a button
        if (other.CompareTag("ColorButton"))
        {
            // Get the material of the collided button (Make sure all buttons have this)
            Material buttonMaterial = other.GetComponent<Renderer>().material;

            // Apply the material to the player's body
            playerRenderer.material = buttonMaterial;

            // Apply the material to both arms
            foreach (Renderer armRenderer in armRenderers)
            {
                armRenderer.material = buttonMaterial;
            }

            Debug.Log("Player touched a color button and changed color to: " + buttonMaterial.name);
        }
    }
}

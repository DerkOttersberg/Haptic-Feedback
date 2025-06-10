using System.Collections;
using UnityEngine;

public class ViewSwitch : MonoBehaviour
{
    public Transform firstPersonPosition;
    public Transform thirdPersonPosition;
    public Transform mainCamera;
    public KeyCode switchKey = KeyCode.C;
    private bool isFirstPerson = false;

    void Start()
    {
        // Set initial camera position to third-person view
        SwitchToThirdPerson();
    }

    void Update()
    {
        if (Input.GetKeyDown(switchKey))
        {
            if (isFirstPerson)
            {
                SwitchToThirdPerson();
            }
            else
            {
                SwitchToFirstPerson();
            }
        }
    }

    void SwitchToFirstPerson()
    {
        isFirstPerson = true;
        StopAllCoroutines();
        StartCoroutine(MoveCamera(firstPersonPosition));
    }

    void SwitchToThirdPerson()
    {
        isFirstPerson = false;
        StopAllCoroutines();
        StartCoroutine(MoveCamera(thirdPersonPosition));
    }

    IEnumerator MoveCamera(Transform targetPosition)
    {
        float elapsedTime = 0f;
        float transitionTime = 0.5f; // Adjust for faster or slower transitions

        Vector3 startingPosition = mainCamera.localPosition;
        Quaternion startingRotation = mainCamera.localRotation;

        while (elapsedTime < transitionTime)
        {
            mainCamera.localPosition = Vector3.Lerp(startingPosition, targetPosition.localPosition, (elapsedTime / transitionTime));
            mainCamera.localRotation = Quaternion.Slerp(startingRotation, targetPosition.localRotation, (elapsedTime / transitionTime));
            elapsedTime += Time.deltaTime;
            yield return null;
        }

        mainCamera.localPosition = targetPosition.localPosition;
        mainCamera.localRotation = targetPosition.localRotation;
    }
}

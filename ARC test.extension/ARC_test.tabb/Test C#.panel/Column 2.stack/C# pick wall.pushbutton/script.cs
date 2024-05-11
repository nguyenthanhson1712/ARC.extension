using System;
using Autodesk.Revit.UI;
using Autodesk.Revit.DB;

using pyRevitLabs.NLog;

namespace PickObjectExample
{
    public class PickObjectCommand : IExternalCommand
    {
        // Define the logger field
        private Logger logger = LogManager.GetCurrentClassLogger();

        public Result Execute(ExternalCommandData revit, ref string message, ElementSet elements)
        {
            // Get the active Revit document
            Document doc = revit.Application.ActiveUIDocument.Document;

            // Create a reference to pick an object
            Reference pickedObjectRef = revit.Application.ActiveUIDocument.Selection.PickObject(Autodesk.Revit.UI.Selection.ObjectType.Element);

            if (pickedObjectRef != null)
            {
                // Get the element ID of the picked object
                ElementId elementId = pickedObjectRef.ElementId;

                // Get the element corresponding to the picked object
                Element pickedElement = doc.GetElement(elementId);

                if (pickedElement != null)
                {
                    // Get the ID of the picked element
                    string elementIdString = pickedElement.Id.ToString();

                    // Log the ID of the picked element
                  //   logger.Info($"Picked object ID: {elementIdString}");

                    // Show a TaskDialog with the ID of the picked object
                    TaskDialog.Show("Picked Object ID", $"ID của đối tượng đã chọn là: {elementIdString}");
                }
                else
                {
                    // Log if the picked element is null
                    logger.Warn("Không thể lấy đối tượng được chọn.");
                }
            }
            else
            {
                // Log if no object is picked
                logger.Warn("Không có đối tượng nào được chọn.");
            }

            return Result.Succeeded;
        }
    }
}

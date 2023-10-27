bl_info = {
    "name": "Go to Frame",
    "author": "tintwotin",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "Sequencer > View > Navigation > Go to Frame",
    "description": "Go to Frame",
    "warning": "",
    "doc_url": "",
    "category": "Sequencer",
}

import bpy
from bpy.utils import smpte_from_frame


class SEQUENCER_OT_frame_current_popup(bpy.types.Operator):
    bl_idname = "sequencer.frame_current_popup"
    bl_label = "Go to Frame"
    bl_options = {"REGISTER", "UNDO"}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=170)

    def execute(self, context):
        return {"FINISHED"}

    def draw(self, context):
        layout = self.layout
        layout.use_property_decorate = True

        # Get the active scene for frame_current property
        active_scene = context.scene
        row = layout.row(align=True)
        row.prop(active_scene, "frame_current", text="", emboss=False)
        row.label(text="%14s" % smpte_from_frame(context.scene.frame_current))


def menu_func(self, context):
    layout = self.layout
    layout.separator()
    layout.operator("sequencer.frame_current_popup")


def register():
    bpy.utils.register_class(SEQUENCER_OT_frame_current_popup)

    # Append the operator to SEQUENCER_MT_navigation
    bpy.types.SEQUENCER_MT_navigation.append(menu_func)


def unregister():
    bpy.utils.unregister_class(SEQUENCER_OT_frame_current_popup)

    # Remove the operator from SEQUENCER_MT_navigation
    bpy.types.SEQUENCER_MT_navigation.remove(menu_func)


if __name__ == "__main__":
    register()

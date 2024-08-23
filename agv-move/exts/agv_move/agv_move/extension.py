import os
import omni.ext
import omni.ui as ui
import omni.graph.core as og
from pxr import Sdf


# Functions and vars are available to other extension as usual in python: `example.python_ext.some_public_function(x)`
def some_public_function(x: int):
    print("[agv_move] some_public_function was called with x: ", x)
    return x ** x


# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class Agv_moveExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self):
        print("[agv_move] agv_move startup")
        manager = omni.kit.app.get_app().get_extension_manager()
        extension_data_path = os.path.join(manager.get_extension_path_by_module("avg_move"), "data")

        self._window = ui.Window("My Window", width=300, height=300)
        with self._window.frame:
            with ui.VStack():
                def on_click():
                    keys = og.Controller.Keys
                    og.Controller.edit(
                        {},
                        {
                            keys.CREATE_NODES: [
                                ("on_move_mode_event", "omni.graph.action.OnMessageBusEvent"),
                                ("read_max_velocity", "omni.graph.core.ReadVariable"),
                                ("write_max_velocity", "omni.graph.core.WriteVariable"),
                                ("on_max_velocity_event", "omni.graph.action.OnMessageBusEvent"),
                                ("compute_wheels_velocities", "omni.graph.scriptnode.ScriptNode"),
                                ("write_L_wheel_velocity", "omni.graph.nodes.WritePrimAttribute"),
                                ("write_R_wheel_velocity", "omni.graph.nodes.WritePrimAttribute"),
                                ("on_key_W", "omni.graph.action.OnKeyboardInput"),
                                ("on_key_S", "omni.graph.action.OnKeyboardInput"),
                                ("on_key_A", "omni.graph.action.OnKeyboardInput"),
                                ("on_key_D", "omni.graph.action.OnKeyboardInput"),
                                ("on_key_Z", "omni.graph.action.OnKeyboardInput"),
                                ("on_key_E", "omni.graph.action.OnKeyboardInput"),
                                ("on_key_Q", "omni.graph.action.OnKeyboardInput"),
                                ("send_forward_mode", "omni.graph.action.SendMessageBusEvent"),
                                ("send_backward_mode", "omni.graph.action.SendMessageBusEvent"),
                                ("send_turnLeft_mode", "omni.graph.action.SendMessageBusEvent"),
                                ("send_turnRight_mode", "omni.graph.action.SendMessageBusEvent"),
                                ("send_brake_mode", "omni.graph.action.SendMessageBusEvent"),
                                ("send_forwardLeft_mode", "omni.graph.action.SendMessageBusEvent"),
                                ("send_forwardRight_mode", "omni.graph.action.SendMessageBusEvent"),
                                ("on_key_1", "omni.graph.action.OnKeyboardInput"),
                                ("on_key_2", "omni.graph.action.OnKeyboardInput"),
                                ("on_key_3", "omni.graph.action.OnKeyboardInput"),
                                ("on_key_4", "omni.graph.action.OnKeyboardInput"),
                                ("send_200_max_velocity", "omni.graph.action.SendMessageBusEvent"),
                                ("send_400_max_velocity", "omni.graph.action.SendMessageBusEvent"),
                                ("send_600_max_velocity", "omni.graph.action.SendMessageBusEvent"),
                                ("send_800_max_velocity", "omni.graph.action.SendMessageBusEvent"),
                            ],
                            keys.CREATE_ATTRIBUTES: [
                                ("compute_wheels_velocities.inputs:mode", "string"),
                                ("compute_wheels_velocities.inputs:max_velocity", "float"),
                            ],
                            keys.SET_VALUES: [
                                ("script_node.inputs:usePath", True),
                                ("script_node.inputs:scriptPath", os.path.join(extension_data_path, "createbox.py")),
                                ("script_node.inputs:location", (x, y, z)),
                                ("script_node.inputs:index", count),
                                ("on_stage_event.inputs:eventName", "Simulation Stop Play"),
                                ("delete_box_node.inputs:usePath", True),
                                ("delete_box_node.inputs:scriptPath", os.path.join(extension_data_path, "delete_box.py")),
                                ("delete_box_node.inputs:graph_path", f"/action_graph_{count}"),
                                ("on_move_mode_event.inputs:eventName", "agv_move_event"),
                                ("read_max_velocity.inputs:variableName", "max_velocity"),
                                ("write_max_velocity.inputs:variableName", "max_velocity"),
                                ("on_max_velocity_event.inputs:eventName", "agv_move_event"),
                                ("compute_wheels_velocities.inputs:usePath", True),
                                ("compute_wheels_velocities.inputs:scriptPath", os.path.join(extension_data_path, "wheels.py")),
                                ("write_L_wheel_velocity.inputs:prim", [Sdf.Path('/World/cast_AGV3/Geometry/RevoluteJoint_MOVE_L')]),
                                ("write_L_wheel_velocity.inputs:name", "drive:angular:physics:targetVelocity"),
                                ("write_R_wheel_velocity.inputs:prim", [Sdf.Path('/World/cast_AGV3/Geometry/RevoluteJoint_MOVE_R')]),
                                ("write_R_wheel_velocity.inputs:name", "drive:angular:physics:targetVelocity"),
                                ("on_key_W.inputs:keyIn", "W"),
                                ("on_key_S.inputs:keyIn", "S"),
                                ("on_key_A.inputs:keyIn", "A"),
                                ("on_key_D.inputs:keyIn", "D"),
                                ("on_key_Z.inputs:keyIn", "Z"),
                                ("on_key_E.inputs:keyIn", "E"),
                                ("on_key_Q.inputs:keyIn", "Q"),
                                ("send_forward_mode.inputs:eventNamt", "agv_move_event"),
                                ("send_forward_mode.inputs:mode", "forward"),
                                ("send_backward_mode.inputs:eventNamt", "agv_move_event"),
                                ("send_backward_mode.inputs:mode", "backward"),
                                ("send_turnLeft_mode.inputs:eventNamt", "agv_move_event"),
                                ("send_turnLeft_mode.inputs:mode", "turnLeft"),
                                ("send_turnRight_mode.inputs:eventNamt", "agv_move_event"),
                                ("send_turnRight_mode.inputs:mode", "turnRight"),
                                ("send_brake_mode.inputs:eventNamt", "agv_move_event"),
                                ("send_brake_mode.inputs:mode", "brake"),
                                ("send_forwardLeft_mode.inputs:eventNamt", "agv_move_event"),
                                ("send_forwardLeft_mode.inputs:mode", "forwardLeft"),
                                ("send_forwardRight_mode.inputs:eventNamt", "agv_move_event"),
                                ("send_forwardRight_mode.inputs:mode", "forwardRight"),
                                ("on_key_1.inputs:keyIn", "Key1"),
                                ("on_key_2.inputs:keyIn", "Key2"),
                                ("on_key_3.inputs:keyIn", "Key3"),
                                ("on_key_4.inputs:keyIn", "Key4"),
                                ("send_200_max_velocity.inputs:eventNamt", "agv_setting_event"),
                                ("send_200_max_velocity.inputs:max_velocity", 200),
                                ("send_400_max_velocity.inputs:eventNamt", "agv_setting_event"),
                                ("send_400_max_velocity.inputs:max_velocity", 400),
                                ("send_600_max_velocity.inputs:eventNamt", "agv_setting_event"),
                                ("send_600_max_velocity.inputs:max_velocity", 600),
                                ("send_800_max_velocity.inputs:eventNamt", "agv_setting_event"),
                                ("send_800_max_velocity.inputs:max_velocity", 800),
                            ],
                            keys.CONNECT: [
                                ("on_move_mode_event.outputs:execOut", "compute_wheels_velocities.inputs:execIn"),
                                ("on_move_mode_event.outputs:mode", "compute_wheels_velocities.inputs:mode"),
                                ("read_max_velocity.outputs:value", "compute_wheels_velocities.inputs:max_velocity"),
                                ("write_max_velocity.outputs:execOut", "compute_wheels_velocities.inputs:execIn"),
                                ("on_max_velocity_event.outputs:execOut", "write_max_velocity.inputs:execIn"),
                                ("on_max_velocity_event.outputs:max_velocity", "write_max_velocity.inputs:value"),
                                ("compute_wheels_velocities.outputs:execOut", "write_L_wheel_velocity.inputs:execIn"),
                                ("compute_wheels_velocities.outputs:execOut", "write_R_wheel_velocity.inputs:execIn"),
                                ("compute_wheels_velocities.outputs:left_target_velocity", "write_L_wheel_velocity.inputs:value"),
                                ("compute_wheels_velocities.outputs:right_target_velocity", "write_R_wheel_velocity.inputs:value"),
                                ("on_key_W.outputs:pressed", "send_forward_mode.inputs:execIn"),
                                ("on_key_S.outputs:pressed", "send_backward_mode.inputs:execIn"),
                                ("on_key_A.outputs:pressed", "send_turnLeft_mode.inputs:execIn"),
                                ("on_key_D.outputs:pressed", "send_turnRight_mode.inputs:execIn"),
                                ("on_key_Z.outputs:pressed", "send_brake_mode.inputs:execIn"),
                                ("on_key_E.outputs:pressed", "send_forwardLeft_mode.inputs:execIn"),
                                ("on_key_Q.outputs:pressed", "send_forwardRight_mode.inputs:execIn"),
                                ("on_key_1.outputs:pressed", "send_200_max_velocity.inputs:execIn"),
                                ("on_key_2.outputs:pressed", "send_400_max_velocity.inputs:execIn"),
                                ("on_key_3.outputs:pressed", "send_600_max_velocity.inputs:execIn"),
                                ("on_key_4.outputs:pressed", "send_800_max_velocity.inputs:execIn"),
                            ]
                        }
                    )

                with ui.HStack():
                    ui.Button("Build Action Graph", clicked_fn=on_click)

    def on_shutdown(self):
        print("[agv_move] agv_move shutdown")

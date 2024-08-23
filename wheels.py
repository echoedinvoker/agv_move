def setup(db: og.Database):
    pass

def cleanup(db: og.Database):
    pass

def compute(db: og.Database):
    mode = db.inputs.mode
    max_velocity = db.inputs.max_velocity

    if mode == 'forward':
        db.outputs.left_target_velocity = -max_velocity
        db.outputs.right_target_velocity = max_velocity
    elif mode == 'backward':
        db.outputs.left_target_velocity = max_velocity
        db.outputs.right_target_velocity = -max_velocity
    elif mode == 'brake':
        db.outputs.left_target_velocity = 0.0
        db.outputs.right_target_velocity = 0.0
    elif mode == 'turnRight':
        db.outputs.left_target_velocity = -max_velocity * 0.3
        db.outputs.right_target_velocity = -max_velocity * 0.3
    elif mode == 'turnLeft':
        db.outputs.left_target_velocity = max_velocity * 0.3
        db.outputs.right_target_velocity = max_velocity * 0.3
    elif mode == 'forwardRight':
        db.outputs.left_target_velocity = -max_velocity
        db.outputs.right_target_velocity = max_velocity * 0.7
    elif mode == 'forwardLeft':
        db.outputs.left_target_velocity = -max_velocity * 0.7
        db.outputs.right_target_velocity = max_velocity
    else:
        left_target_velocity, db.outputs.right_target_velocity = map(float, mode.split(','))
        db.outputs.left_target_velocity = -1 * left_target_velocity

    return True

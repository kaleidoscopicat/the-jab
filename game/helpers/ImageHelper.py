# @name: ImageHelper.py
# @desc: Pure merge of generate_hitbox_based_of_of_image.py and import_spritesheet.py
#        Intended to be used as a module to be imported!

## @last-modified: 1:19 19/10/25
## | Merged "generate_hitbox_based_of_of_image.py" && "import_spritesheet.py"

import pygame
from main import _hitbox_cache

def load_spritesheet_images(spritesheet_path, sprite_width, sprite_height, frames_per_row, total_frames=None,
                            scale=None):
    try:
        sheet = pygame.image.load(spritesheet_path).convert_alpha()
    except pygame.error as e:
        print(f"Unable to load spritesheet: {spritesheet_path}")
        raise SystemExit(e)

    images = []
    sheet_width = sheet.get_width()
    sheet_height = sheet.get_height()

    max_cols = sheet_width // sprite_width
    max_rows = sheet_height // sprite_height
    max_frames = max_cols * max_rows

    if total_frames is None:
        total_frames = max_frames
    else:
        total_frames = min(total_frames, max_frames)

    frame_count = 0
    row = 0
    col = 0

    while frame_count < total_frames:
        x = col * sprite_width
        y = row * sprite_height

        if x + sprite_width > sheet_width or y + sprite_height > sheet_height:
            break

        image = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA)
        image.blit(sheet, (0, 0), (x, y, sprite_width, sprite_height))

        if scale:
            image = pygame.transform.scale(image, scale)

        images.append(image)
        frame_count += 1

        col += 1
        if col >= frames_per_row:
            col = 0
            row += 1

    return images

def generate_hitbox(image, x, y):
    cache_key = (image.get_size(), id(image))

    if cache_key not in _hitbox_cache:
        if image.get_flags() & pygame.SRCALPHA == 0:
            temp = pygame.Surface(image.get_size(), pygame.SRCALPHA)
            temp.blit(image, (0, 0))
            image = temp

        mask = pygame.mask.from_surface(image)

        ## Gentle cleanup...
        if mask.count() == 0 or not mask.get_bounding_rects():
            rect = image.get_rect()
            _hitbox_cache[cache_key] = rect
        else:
            bounds = mask.get_bounding_rects()
            hitbox = bounds[0].unionall(bounds[1:]) if len(bounds) > 1 else bounds[0]
            _hitbox_cache[cache_key] = hitbox

    cached_rect = _hitbox_cache[cache_key].copy()
    cached_rect.x = x
    cached_rect.y = y
    return cached_rect
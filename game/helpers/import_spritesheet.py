import pygame

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

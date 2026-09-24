import asyncio, re, pathlib
from playwright.async_api import async_playwright
HERE = pathlib.Path(__file__).resolve().parent
src = HERE / "svg"                      # gen/figs/svg/*.svg
dst = HERE.parent.parent / "img"        # リポジトリ直下の img/ に PNG を書く
dst.mkdir(exist_ok=True)
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for f in sorted(src.glob("*.svg")):
            svg = f.read_text()
            w = int(re.search(r'width="(\d+)"', svg).group(1)); h = int(re.search(r'height="(\d+)"', svg).group(1))
            pg = await b.new_page(viewport={"width": w, "height": h}, device_scale_factor=2)
            await pg.set_content(f"<html><body style='margin:0;background:white'>{svg}</body></html>")
            await pg.wait_for_timeout(300)
            await pg.screenshot(path=str(dst / f"{f.stem}.png"))
            print(f.stem, w, h)
        await b.close()
asyncio.run(main())

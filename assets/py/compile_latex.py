import subprocess
import os
import tempfile
import shutil
import argparse

def compile_latex(tex_file):
    if not os.path.isfile(tex_file):
        print(f"Error: File '{tex_file}' not found.")
        return

    tex_file = os.path.abspath(tex_file)
    tex_dir = os.path.dirname(tex_file)
    tex_filename = os.path.basename(tex_file)
    tex_basename = os.path.splitext(tex_filename)[0]  

    tmpdir = tempfile.mkdtemp()

    try:
        shutil.copytree(tex_dir,tmpdir,dirs_exist_ok=True)

        old_cwd = os.getcwd()
        os.chdir(tmpdir)
        subprocess.run(["pdflatex", tex_filename], check=True)

        bib_file = tex_basename + ".aux"
        if os.path.exists(bib_file):
            subprocess.run(["bibtex", tex_basename], check=True)
        
        subprocess.run(["pdflatex", tex_filename], check=True)
        subprocess.run(["pdflatex", tex_filename], check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error during compilation: {e}")

    finally:
        pdf_name = tex_basename + ".pdf"
        pdf_path = os.path.join(tmpdir, pdf_name)
        final_pdf_path = os.path.join(old_cwd, pdf_name)

        if os.path.exists(pdf_path):
            shutil.move(pdf_path, final_pdf_path)
            print(f"Compilation successful! PDF saved as: {final_pdf_path}")
        else:
            print("Compilation failed: No PDF generated.")
        os.chdir(old_cwd)
        shutil.rmtree(tmpdir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compile a LaTeX document using pdflatex and bibtex.")
    parser.add_argument("tex_file", help="Path to the LaTeX file")
    args = parser.parse_args()
    compile_latex(args.tex_file)

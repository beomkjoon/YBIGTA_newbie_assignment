# anaconda(또는 miniconda)가 존재하지 않을 경우 설치해주세요!
## TODO
if ! command -v conda &> /dev/null; then
    echo "[INFO] conda가 설치되어 있지 않습니다. Miniconda를 설치합니다."
    wget -q https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
    bash ~/miniconda.sh -b -p "$HOME/miniconda"
    rm ~/miniconda.sh
    export PATH="$HOME/miniconda/bin:$PATH"
fi

source "$(conda info --base)/etc/profile.d/conda.sh"

# Conda 환셩 생성 및 활성화
## TODO
if ! conda env list | grep -q "myenv"; then
    echo "[INFO] myenv 가상환경을 생성합니다."
    conda create -y -n myenv python=3.9
fi
conda activate myenv

## 건드리지 마세요! ##
python_env=$(python -c "import sys; print(sys.prefix)")
if [[ "$python_env" == *"/envs/myenv"* ]]; then
    echo "[INFO] 가상환경 활성화: 성공"
else
    echo "[INFO] 가상환경 활성화: 실패"
    exit 1 
fi

# 필요한 패키지 설치
## TODO
pip install --quiet mypy

# Submission 폴더 파일 실행
cd submission || { echo "[INFO] submission 디렉토리로 이동 실패"; exit 1; }

for file in *.py; do
    ## TODO
    problem_number=$(echo "$file" | cut -d'_' -f2 | cut -d'.' -f1)
    input_path="../input/${problem_number}_input"
    output_path="../output/${problem_number}_output"

    if [[ -f "$input_path" ]]; then
        echo "[INFO] 실행: $file (input: ${problem_number}_input)"
        python "$file" < "$input_path" > "$output_path"
    else
        echo "[INFO] input 파일이 없어 그냥 실행: $file"
        python "$file" > "$output_path"
    fi
done

# mypy 테스트 실행 및 mypy_log.txt 저장
## TODO
mypy . > ../mypy_log.txt

# conda.yml 파일 생성
## TODO
conda env export > ../conda.yml

# 가상환경 비활성화
## TODO
conda deactivate
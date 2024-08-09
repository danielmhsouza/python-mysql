Aluno:dict = {
    "id": [],
    "nome":[],
    "idade":[]
}

def InserirAluno(nome:str, idade:str):
    assert nome != None and idade != None, "Os campos são obrigatórios."
    
    new_id:int = len(Aluno["id"])
    Aluno["id"].append(new_id+1)
    Aluno["nome"].append(nome)
    Aluno["idade"].append(idade)
    print("Aluno inserido com sucesso")
    

def SelecionarAlunoPorID(id:int) -> dict:
    return {"id": id, "nome":Aluno["nome"][id-1], "idade":Aluno["idade"][id-1]}

def main():
    InserirAluno("Daniel", 12)
    InserirAluno("Lucas", 18)
    InserirAluno("Felipe", 80)
    print(Aluno)
    
    print(SelecionarAlunoPorID(2))
    
main()
from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    # program: decls EOF;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decls()))

    def visitDecls(self, ctx: MT22Parser.DeclsContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.decl())
        return self.visit(ctx.decls()) + self.visit(ctx.decl())

    def visitDecl(self, ctx: MT22Parser.DeclContext):
        # decl: function | vardecl ;
        if ctx.function():
            return self.visit(ctx.function())
        return self.visit(ctx.vardecl())

    def visitFunction(self, ctx: MT22Parser.FunctionContext):
        # function: ID COLO FUNC systemtype LB listparam? RB (INHERIT ID)? blocksta  ;
        name = ctx.ID(0).getText()
        typ = self.visit(ctx.systemtype())
        body = self.visit(ctx.blocksta())
        paramlist = []
        if ctx.listparam():
            paramlist = self.visit(ctx.listparam())
        id1 = None
        if ctx.INHERIT():
            id1 = ctx.ID(1).getText()
        return [FuncDecl(name, typ, paramlist, id1, body)]

    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        # vardecl: (noninitvardecl | initvardecl ) SEMI  ;
        if ctx.noninitvardecl():
            return self.visit(ctx.noninitvardecl())
        return self.visit(ctx.initvardecl())

    def visitNoninitvardecl(self, ctx: MT22Parser.NoninitvardeclContext):
        # noninitvardecl: idlist COLO  (autotype | arrtype)  ;
        ids = self.visit(ctx.idlist())
        mptype = None
        if ctx.autotype():
            mptype = self.visit(ctx.autotype())
        elif ctx.arrtype():
            mptype = self.visit(ctx.arrtype())
        res = []
        for x in ids:
            res += [VarDecl(x, mptype, None)]
        return res

    def visitInitvardecl(self, ctx: MT22Parser.InitvardeclContext):
        # initvardecl: ID initvardeclrec exp0;
        id = ctx.ID().getText()
        if ctx.exp0():
            expr = self.visit(ctx.exp0())
        else:
            t = self.visit(ctx.specialfunc())
            expr = FuncCall(t["name"], t["param"])
        res = {"name": [id], "type": None, "listexp": [expr]}
        self.res = res
        res = self.visit(ctx.initvardeclrec())
        l = []
        leng = len(res["name"])
        for x in range(0, leng):
            l += [VarDecl(res["name"][x], res["type"],
                          res["listexp"][leng - x-1])]
        return l

    def visitInitvardeclrec(self, ctx: MT22Parser.InitvardeclrecContext):
        # COMMA ID initvardeclrec exp0 COMMA| COLO (autotype | arrtype) ASG;
        typ = None
        res = self.res
        if ctx.initvardeclrec():
            name = ctx.ID().getText()
            if ctx.exp0():
                exp = self.visit(ctx.exp0())
            else:
                t = self.visit(ctx.specialfunc())
                exp = FuncCall(t["name"], t["param"])
            res["name"].append(name)
            res["listexp"].append(exp)
            self.res = res
            return self.visit(ctx.initvardeclrec())
        else:
            if ctx.autotype():
                typ = self.visit(ctx.autotype())
            else:
                typ = self.visit(ctx.arrtype())
            res["type"] = typ
        self.res = res
        return res

    def visitStmt(self, ctx: MT22Parser.StmtContext):
        # stmt:	assginsta	| ifst	| forsta	| contista	| breaksta	| returnsta	| blocksta	| callstmt	| vardecl	| dosta	| whilesta	| spefunc_stmt;
        if ctx.assginsta():
            return self.visit(ctx.assginsta())
        elif ctx.ifsta():
            return self.visit(ctx.ifsta())
        elif ctx.forsta():
            return self.visit(ctx.forsta())
        elif ctx.contista():
            return self.visit(ctx.contista())
        elif ctx.breaksta():
            return self.visit(ctx.breaksta())
        elif ctx.returnsta():
            return self.visit(ctx.returnsta())
        elif ctx.blocksta():
            return self.visit(ctx.blocksta())
        elif ctx.callstmt():
            return self.visit(ctx.callstmt())
        elif ctx.vardecl():
            return self.visit(ctx.vardecl())
        elif ctx.dosta():
            return self.visit(ctx.dosta())
        elif ctx.whilesta():
            return self.visit(ctx.whilesta())
        return self.visit(ctx.spefuncstmt())

    def visitSpefuncstmt(self, ctx:  MT22Parser.SpefuncstmtContext):
        t = self.visit(ctx.specialfunc())
        return CallStmt(t["name"], t["param"])

    def visitSpecialfunc(self, ctx:  MT22Parser.SpecialfuncContext):
        # specialfunc: (readInt | printInt | readFloat | writeFloat |printBool | readString | printString | superfunc | predef ) ;
        if ctx.readInt():
            return self.visit(ctx.readInt())
        if ctx.printInt():
            return self.visit(ctx.printInt())
        if ctx.readFloat():
            return self.visit(ctx.readFloat())
        if ctx.writeFloat():
            return self.visit(ctx.writeFloat())
        if ctx.printBool():
            return self.visit(ctx.printBool())
        if ctx.readString():
            return self.visit(ctx.readString())
        if ctx.printString():
            return self.visit(ctx.printString())
        if ctx.superfunc():
            return self.visit(ctx.superfunc())
        if ctx.predef():
            return self.visit(ctx.predef())
        if ctx.readBool():
            return self.visit(ctx.readBool())

    def visitCallstmt(self, ctx: MT22Parser.CallstmtContext):
        # callstmt: ID LB listexp? RB SEMI ;
        listexp = []
        if ctx.listexp():
            listexp = self.visit(ctx.listexp())
        return CallStmt(ctx.ID().getText(), listexp)

    def visitAssginsta(self, ctx: MT22Parser.AssginstaContext):
        # assginsta: lhs ASG (exp0 | specialfunc | funcall) SEMI;
        lhs = self.visit(ctx.lhs())
        rhs = None
        if ctx.exp0():
            rhs = self.visit(ctx.exp0())
        elif ctx.funcall():
            rhs = self.visit(ctx.funcall())
        else:
            rhs = self.visit(ctx.specialfunc())
            rhs = FuncCall(rhs["name"], rhs["param"])
        return AssignStmt(lhs, rhs)

    def visitLhs(self, ctx: MT22Parser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.exp7())

    def visitIfsta(self, ctx: MT22Parser.IfstaContext):
        # ifsta:	IF LB exp0 RB stmt (ELSE stmt)?;
        fstmt = None
        if ctx.ELSE():
            fstmt = self.visit(ctx.stmt(1))
        cond = self.visit(ctx.exp0())
        tstmt = self.visit(ctx.stmt(0))
        return IfStmt(cond, tstmt, fstmt)

    def visitForsta(self, ctx: MT22Parser.ForstaContext):
        # forsta: FOR LB lhs ASG exp0 COMMA exp1 COMMA exp0 RB stmt ;
        lhs = self.visit(ctx.lhs())
        rhs = self.visit(ctx.exp0(0))
        init = AssignStmt(lhs, rhs)
        cond = self.visit(ctx.exp1())
        upd = self.visit(ctx.exp0(1))
        stmt = self.visit(ctx.stmt())
        return ForStmt(init, cond, upd, stmt)

    def visitContista(self, ctx: MT22Parser.ContistaContext):
        return ContinueStmt()

    def visitBreaksta(self, ctx: MT22Parser.BreakstaContext):
        # breaksta: BREAK SEMI;
        return BreakStmt()

    def visitReturnsta(self, ctx: MT22Parser.ReturnstaContext):
        # returnsta: RETURN exp0? SEMI;
        expr = None
        if ctx.exp0():
            expr = self.visit(ctx.exp0())
        return ReturnStmt(expr)

    def visitWhilesta(self, ctx: MT22Parser.WhilestaContext):
        # whilesta: WHILE LB exp0 RB blocksta ;
        expr = self.visit(ctx.exp0())
        block = self.visit(ctx.blocksta()) if ctx.blocksta(
        ) else self.visit(ctx.stmt())
        return WhileStmt(expr, block)

    def visitDosta(self, ctx: MT22Parser.DostaContext):
        # dosta: DO blocksta WHILE LB exp0 RB  SEMI;
        block = self.visit(ctx.blocksta()) if ctx.blocksta(
        ) else self.visit(ctx.stmt())
        return DoWhileStmt(self.visit(ctx.exp0()), block)

    def visitBlocksta(self, ctx: MT22Parser.BlockstaContext):
        # blocksta: LP body1 RP;
        nested_list = self.visit(ctx.body1())

        if nested_list:
            listexp = [item for sublist in nested_list for item in (
                sublist if isinstance(sublist, list) else [sublist])]
        else:
            listexp = []

        return BlockStmt(listexp)

    def visitBody1(self, ctx: MT22Parser.Body1Context):
        # body1: body1 stmt | stmt |  ;
        if ctx.getChildCount() == 0:
            return
        elif ctx.getChildCount() == 1:
            return [self.visit(ctx.stmt())]
        return self.visit(ctx.body1()) + [self.visit(ctx.stmt())]
        # l = None
        # # body1: body1 stmt | stmt |  ;
        # if ctx.getChildCount() == 0:
        #     return
        # elif ctx.getChildCount() == 1:
        #     l = [self.visit(ctx.stmt())]

        # else:
        #     l = self.visit(ctx.body1()) + [self.visit(ctx.stmt())]
        # return [item for sublist in l for item in sublist]

    def visitListparam(self, ctx: MT22Parser.ListparamContext):
        # listparam: listparam COMMA paramemter | paramemter;
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.paramemter())]
        return self.visit(ctx.listparam()) + [self.visit(ctx.paramemter())]

    def visitParamemter(self, ctx: MT22Parser.ParamemterContext):
        # paramemter: INHERIT?  OUT? ID COLO (autotype | arrtype) ;
        inherit = False
        out = False
        if ctx.INHERIT():
            inherit = True
        if ctx.OUT():
            out = True
        typ = None
        if ctx.autotype():
            typ = self.visit(ctx.autotype())
        else:
            typ = self.visit(ctx.arrtype())
        name = ctx.ID().getText()
        return ParamDecl(name, typ, out, inherit)

    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        # idlist: ID COMMA idlist | ID;
        if ctx.getChildCount() == 1:
            return [ctx.ID().getText()]
        return [ctx.ID().getText()] + self.visit(ctx.idlist())

    def visitReadInt(self, ctx: MT22Parser.ReadIntContext):
        return {"name": ctx.READINT().getText(), "param": []}

    def visitPrintInt(self, ctx: MT22Parser.PrintIntContext):
        param = []
        if ctx.INT():
            param = [IntegerLit(int(ctx.INT().getText()))]
        elif ctx.ID():
            param = [Id(ctx.ID().getText())]
        elif ctx.exp0():
            param = [self.visit(ctx.exp0())]

        return {"name": ctx.PRINTINT().getText(), "param": param}

    def visitReadFloat(self, ctx: MT22Parser.ReadFloatContext):
        return {"name": ctx.READF().getText(), "param": []}

    def visitWriteFloat(self, ctx: MT22Parser.WriteFloatContext):
        if ctx.FLOATLIT():
            param = [FloatLit(float(ctx.FLOATLIT().getText()))]
        elif ctx.ID():
            param = [Id(ctx.ID().getText())]
        elif ctx.exp0():
            param = [self.visit(ctx.exp0())]
        return {"name": ctx.WRITEF().getText(), "param": param}

    def visitPrintBool(self, ctx: MT22Parser.PrintBoolContext):
        if ctx.boolit():
            param = [self.visit(ctx.boolit())]
        elif ctx.ID():
            param = [Id(ctx.ID().getText())]
        elif ctx.exp0():
            param = [self.visit(ctx.exp0())]
        return {"name": ctx.PRINTBOOL().getText(), "param": param}

    def visitReadString(self, ctx: MT22Parser.ReadStringContext):
        return {"name": ctx.READSTRING().getText(), "param": []}

    def visitPrintString(self, ctx: MT22Parser.PrintStringContext):
        if ctx.STRLIT():
            param = [StringLit(ctx.STRLIT().getText())]
        elif ctx.ID():
            param = [Id(ctx.ID().getText())]
        elif ctx.exp0():
            param = [self.visit(ctx.exp0())]
        return {"name": ctx.PRINTSTRING().getText(), "param": param}

    def visitSuperfunc(self, ctx: MT22Parser.SuperfuncContext):
        listexp = self.visit(ctx.listexp())
        return {"name": ctx.SUPER().getText(), "param": listexp}

    def visitPredef(self, ctx: MT22Parser.PredefContext):
        return {"name": ctx.PREDE().getText(), "param": []}

    def visitReadBool(self, ctx: MT22Parser.ReadBoolContext):
        return {"name": ctx.READBOOL().getText(), "param": []}

    def visitListexp(self, ctx: MT22Parser.ListexpContext):
        # listexp:  listexp COMMA exp0 | exp0;
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.exp0())]
        return self.visit(ctx.listexp()) + [self.visit(ctx.exp0())]

    def visitExp0(self, ctx: MT22Parser.Exp0Context):
        # exp0: exp1 CONCAT exp1| exp1;
        if ctx.getChildCount() != 1:
            return BinExpr(ctx.CONCAT(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
        return self.visit(ctx.exp1(0))

    def visitExp1(self, ctx: MT22Parser.Exp1Context):
        # exp1:	exp2 EQUAL exp2	| exp2 NEQUAL exp2	| exp2 LTE exp2	| exp2 GTE exp2	| exp2 LT exp2	| exp2 GT exp2	| exp2;
        if ctx.EQUAL():
            return BinExpr(ctx.EQUAL(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        if ctx.NEQUAL():
            return BinExpr(ctx.NEQUAL(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        if ctx.LTE():
            return BinExpr(ctx.LTE(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        if ctx.GTE():
            return BinExpr(ctx.GTE(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        if ctx.LT():
            return BinExpr(ctx.LT(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        if ctx.GT():
            return BinExpr(ctx.GT(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        return self.visit(ctx.exp2(0))

    def visitExp2(self, ctx: MT22Parser.Exp2Context):
        if ctx.AND():
            return BinExpr(ctx.AND(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))
        if ctx.OR():
            return BinExpr(ctx.OR(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))
        return self.visit(ctx.exp3())

    def visitExp3(self, ctx: MT22Parser.Exp3Context):
        # exp3: exp3 ADD exp4 | exp3 SUB exp4 | exp4;
        if ctx.ADD():
            return BinExpr(ctx.ADD(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        if ctx.SUB():
            return BinExpr(ctx.SUB(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        return self.visit(ctx.exp4())

    def visitExp4(self, ctx: MT22Parser.Exp4Context):
        # exp4: exp4 MUL exp5 | exp4 DIV exp5 | exp4 MOD exp5 | exp5;
        if ctx.MUL():
            return BinExpr(ctx.MUL(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        if ctx.DIV():
            return BinExpr(ctx.DIV(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        if ctx.MOD():
            return BinExpr(ctx.MOD(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        return self.visit(ctx.exp5())

    def visitExp5(self, ctx: MT22Parser.Exp5Context):
        # exp5: NOT exp6 | exp6;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp6())
        return UnExpr(ctx.NOT(), self.visit(ctx.exp5()))

    def visitExp6(self, ctx: MT22Parser.Exp6Context):
        # exp6: SUB exp7 | exp7;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp7())
        return UnExpr(ctx.SUB(), self.visit(ctx.exp6()))

    def visitExp7(self, ctx: MT22Parser.Exp7Context):
        # exp7: ID LS listexp RS | exp8;
        if ctx.exp8():
            return self.visit(ctx.exp8())
        name = ctx.ID().getText()
        listexp = self.visit(ctx.listexp())
        return ArrayCell(name, listexp)

    def visitExp8(self, ctx: MT22Parser.Exp8Context):
        # exp8: 	FLOATLIT	| boolit| STRLIT| ID	| INT	| arr	| exp9	| funcall	;
        if ctx.FLOATLIT():
            return FloatLit(float('0' + ctx.FLOATLIT().getText()))
        if ctx.boolit():
            return self.visit(ctx.boolit())
        if ctx.STRLIT():
            return StringLit(ctx.STRLIT().getText())
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.INT():
            return IntegerLit(int(ctx.INT().getText()))
        if ctx.arr():
            return self.visit(ctx.arr())
        if ctx.exp9():
            return self.visit(ctx.exp9())
        if ctx.arrlit():
            return self.visit(ctx.arrlit())
        return self.visit(ctx.funcall())

    def visitExp9(self, ctx: MT22Parser.Exp9Context):
        # exp9: LB exp0 RB;
        return self.visit(ctx.exp0())

    def visitFuncall(self, ctx: MT22Parser.FuncallContext):
        # funcall: ID LB listexp? RB;
        listexp = []
        if ctx.listexp():
            listexp = self.visit(ctx.listexp())
        name = ctx.ID().getText()
        return FuncCall(name, listexp)

    def visitArrtype(self, ctx: MT22Parser.ArrtypeContext):
        # arrtype: ARRAY LS intlitarr RS OF  autotype ;
        intlitarr = self.visit(ctx.intlitarr())
        typ = self.visit(ctx.autotype())
        return ArrayType(intlitarr, typ)

    # done yet
    def visitArr(self, ctx: MT22Parser.ArrContext):
        # arr: ID LS intlitarr RS ;
        id = ctx.ID().getText()
        inlitarr = self.visit(ctx.intlitarr())

    def visitArrlit(self, ctx: MT22Parser.ArrlitContext):
        # arrlit: LP listexp RP ;

        listexp = self.visit(ctx.listexp()) if ctx.listexp() else []
        return ArrayLit(listexp)

    def visitIntlitarr(self, ctx: MT22Parser.IntlitarrContext):
        # intlitarr: intlitarr COMMA INT | INT;
        if ctx.getChildCount() == 1:
            return [ctx.INT().getText()]
        return self.visit(ctx.intlitarr()) + [ctx.INT().getText()]

    def visitAutotype(self, ctx: MT22Parser.AutotypeContext):
        # autotype: INTEGER  | STRING | BOOLEAN | FLOAT | AUTO  ;
        if ctx.INTEGER():
            return IntegerType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BooleanType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.AUTO():
            return AutoType()

    def visitSystemtype(self, ctx: MT22Parser.SystemtypeContext):
        # systemtype: INTEGER  | STRING | BOOLEAN | FLOAT | 'void' | arrtype | AUTO ;
        if ctx.INTEGER():
            return IntegerType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BooleanType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.arrtype():
            return self.visit(ctx.arrtype())
        elif ctx.AUTO():
            return AutoType()
        return VoidType()

    def visitBoolit(self, ctx: MT22Parser.BoolitContext):
        if ctx.TRUE():
            return BooleanLit(True)
        return BooleanLit(False)

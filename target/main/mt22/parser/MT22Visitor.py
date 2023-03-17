# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decls.
    def visitDecls(self, ctx:MT22Parser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assginsta.
    def visitAssginsta(self, ctx:MT22Parser.AssginstaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callstmt.
    def visitCallstmt(self, ctx:MT22Parser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ifsta.
    def visitIfsta(self, ctx:MT22Parser.IfstaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forsta.
    def visitForsta(self, ctx:MT22Parser.ForstaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#contista.
    def visitContista(self, ctx:MT22Parser.ContistaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#breaksta.
    def visitBreaksta(self, ctx:MT22Parser.BreakstaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnsta.
    def visitReturnsta(self, ctx:MT22Parser.ReturnstaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#whilesta.
    def visitWhilesta(self, ctx:MT22Parser.WhilestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dosta.
    def visitDosta(self, ctx:MT22Parser.DostaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blocksta.
    def visitBlocksta(self, ctx:MT22Parser.BlockstaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#body1.
    def visitBody1(self, ctx:MT22Parser.Body1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#listval.
    def visitListval(self, ctx:MT22Parser.ListvalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#listparam.
    def visitListparam(self, ctx:MT22Parser.ListparamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramemter.
    def visitParamemter(self, ctx:MT22Parser.ParamemterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#noninitvardecl.
    def visitNoninitvardecl(self, ctx:MT22Parser.NoninitvardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#initvardecl.
    def visitInitvardecl(self, ctx:MT22Parser.InitvardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#initvardeclrec.
    def visitInitvardeclrec(self, ctx:MT22Parser.InitvardeclrecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#spefuncstmt.
    def visitSpefuncstmt(self, ctx:MT22Parser.SpefuncstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function.
    def visitFunction(self, ctx:MT22Parser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#specialfunc.
    def visitSpecialfunc(self, ctx:MT22Parser.SpecialfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readInt.
    def visitReadInt(self, ctx:MT22Parser.ReadIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printInt.
    def visitPrintInt(self, ctx:MT22Parser.PrintIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readFloat.
    def visitReadFloat(self, ctx:MT22Parser.ReadFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#writeFloat.
    def visitWriteFloat(self, ctx:MT22Parser.WriteFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printBool.
    def visitPrintBool(self, ctx:MT22Parser.PrintBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readBool.
    def visitReadBool(self, ctx:MT22Parser.ReadBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readString.
    def visitReadString(self, ctx:MT22Parser.ReadStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printString.
    def visitPrintString(self, ctx:MT22Parser.PrintStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#superfunc.
    def visitSuperfunc(self, ctx:MT22Parser.SuperfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#predef.
    def visitPredef(self, ctx:MT22Parser.PredefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#listexp.
    def visitListexp(self, ctx:MT22Parser.ListexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp0.
    def visitExp0(self, ctx:MT22Parser.Exp0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp1.
    def visitExp1(self, ctx:MT22Parser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp2.
    def visitExp2(self, ctx:MT22Parser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp3.
    def visitExp3(self, ctx:MT22Parser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp4.
    def visitExp4(self, ctx:MT22Parser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp5.
    def visitExp5(self, ctx:MT22Parser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp6.
    def visitExp6(self, ctx:MT22Parser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp7.
    def visitExp7(self, ctx:MT22Parser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp8.
    def visitExp8(self, ctx:MT22Parser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp9.
    def visitExp9(self, ctx:MT22Parser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcall.
    def visitFuncall(self, ctx:MT22Parser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrlit.
    def visitArrlit(self, ctx:MT22Parser.ArrlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrtype.
    def visitArrtype(self, ctx:MT22Parser.ArrtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#literals.
    def visitLiterals(self, ctx:MT22Parser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arr.
    def visitArr(self, ctx:MT22Parser.ArrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#intlitarr.
    def visitIntlitarr(self, ctx:MT22Parser.IntlitarrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#autotype.
    def visitAutotype(self, ctx:MT22Parser.AutotypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#systemtype.
    def visitSystemtype(self, ctx:MT22Parser.SystemtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#boolit.
    def visitBoolit(self, ctx:MT22Parser.BoolitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#comment.
    def visitComment(self, ctx:MT22Parser.CommentContext):
        return self.visitChildren(ctx)



del MT22Parser
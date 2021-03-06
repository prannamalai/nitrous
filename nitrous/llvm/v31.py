(VoidTypeKind,
 HalfTypeKind,
 FloatTypeKind,
 DoubleTypeKind,
 X86_FP80TypeKind,
 FP128TypeKind,
 PPC_FP128TypeKind,
 LabelTypeKind,
 IntegerTypeKind,
 FunctionTypeKind,
 StructTypeKind,
 ArrayTypeKind,
 PointerTypeKind,
 VectorTypeKind,
 MetadataTypeKind,
 X86_MMXTypeKind
) = range(16)


(IntEQ,
 IntNE,
 IntUGT,
 IntUGE,
 IntULT,
 IntULE,
 IntSGT,
 IntSGE,
 IntSLT,
 IntSLE,
) = range(32, 42)


(RealPredicateFalse,
 RealOEQ,
 RealOGT,
 RealOGE,
 RealOLT,
 RealOLE,
 RealONE,
 RealORD,
 RealUNO,
 RealUEQ,
 RealUGT,
 RealUGE,
 RealULT,
 RealULE,
 RealUNE,
 RealPredicateTrue
) = range(16)


(CodeGenLevelNone,
 CodeGenLevelLess,
 CodeGenLevelDefault,
 CodeGenLevelAggressive) = range(4)


(RelocDefault,
 RelocStatic,
 RelocPIC,
 RelocDynamicNoPic) = range(4)


(CodeModelDefault,
 CodeModelJITDefault,
 CodeModelSmall,
 CodeModelKernel,
 CodeModelMedium,
 CodeModelLarge) = range(6)


(AssemblyFile,
 ObjectFile) = range(2)

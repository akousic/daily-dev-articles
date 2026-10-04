# Rust's derive often implies inline

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-10-03 20:41
- **Original:** https://yossarian.net/til/post/rust-s-derive-often-implies-inline/

## Summary

In Rust, one of the most common ways to implement core traits (like Debug, Display, and Clone) is to #[derive(...)] them, e.g.: #[derive(Debug)] struct Widgets { foo: u32, bar: usize, } What I didn't know until recently is that Rust currently emits #[inline] as part of these derivations. This is seemingly not guaranteed, but is implied by example in the reference and can also be seen if one expands the macros. Using the example above, this is what you get when you expand the #[derive(Debug)] in the playground: struct Widgets { foo: u32, bar: usize, } #[automatically_derived] impl ::core::fmt::Debug for Widgets { #[inline] fn fmt(&self, f: &mut ::core::fmt::Formatter) -> ::core::fmt::Result { ::core::fmt::Formatter::debug_struct_field2_finish(f, "Widgets", "foo", &self.foo, "bar", &&self.bar) } } This is almost always what we want: #[inline] is just a hint, and typical derived Debug, Clone, etc.

## Key Takeaways

- implementations benefit from being inlined (since they're often trivial).
- Imagine an error hierarchy like this: #[derive(Debug)] struct ErrorA { lots: String, of: String, chunky: String, fields: String, within: String, this: String, r#type: String, } #[derive(Debug)] struct ErrorB { inner: ErrorA, } #[derive(Debug)] struct ErrorC { inner: ErrorB, } #[derive(Debug)] enum Errors { A(ErrorA), B(ErrorB), C(ErrorC), } produces: struct ErrorA { lots: String, of: String, chunky: String, fields: String, within: String, this: String, r#type: String, } #[automatically_derived] impl ::core::fmt::Debug for ErrorA { #[inline] fn fmt(&self, f: &mut ::core::fmt::Formatter) -> ::core::fmt::Result { let names: &'static _ = &["lots", "of", "chunky", "fields", "within", "this", "type"]; let values: &[&dyn ::core::fmt::Debug] = &[&self.lots, &self.of, &self.chunky, &self.fields, &self.within, &self.this, &&self.r#type]; ::core::fmt::Formatter::debug_struct_fields_finish(f, "ErrorA", names, values) } } #[automatically_derived] impl ::core::default::Default for ErrorA { #[inline] fn default() -> Self { Self { lots: ::core::default::Default::default(), of: ::core::default::Default::default(), chunky: ::core::default::Default::default(), fields: ::core::default::Default::default(), within: ::core::default::Default::default(), this: ::core::default::Default::default(), r#type: ::core::default::Default::default(), } } } struct ErrorB { inner: ErrorA, } #[automatically_derived] impl ::core::fmt::Debug for ErrorB { #[inline] fn fmt(&self, f: &mut ::core::fmt::Formatter) -> ::core::fmt::Result { ::core::fmt::Formatter::debug_struct_field1_finish(f, "ErrorB", "inner", &&self.inner) } } struct ErrorC { inner: ErrorB, } #[automatically_derived] impl ::core::fmt::Debug for ErrorC { #[inline] fn fmt(&self, f: &mut ::core::fmt::Formatter) -> ::core::fmt::Result { ::core::fmt::Formatter::debug_struct_field1_finish(f, "ErrorC", "inner", &&self.inner) } } enum Errors { A(ErrorA), B(ErrorB), C(ErrorC), } #[automatically_derived] impl ::core::fmt::Debug for Errors { #[inline] fn fmt(&self, f: &mut ::core::fmt::Formatter) -> ::core::fmt::Result { match self { Self::A(__self_0) => ::core::fmt::Formatter::debug_tuple_field1_finish(f, "A", &__self_0), Self::B(__self_0) => ::core::fmt::Formatter::debug_tuple_field1_finish(f, "B", &__self_0), Self::C(__self_0) => ::core::fmt::Formatter::debug_tuple_field1_finish(f, "C", &__self_0), } } } That's a lot of code that can get inlined for each invocation of the Debug implementation of Errors, which can occur repeatedly in e.g.
- debug or trace logging.

---
_Auto-generated daily digest entry._
